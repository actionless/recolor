import os
import re
import sys
import multiprocessing
import inspect
from functools import partial

from PIL import Image

from common import hex2rgb, rgb2hex
import presets


R = 0
G = 1
B = 2
A = 3


def rgba2str(pixel):
    return "rgba({}, {}, {}, {})".format(*pixel)


def ls(x):
    return list(os.walk(x))[0][2]


def ls_r(path):
    return [
        os.path.join(files[0], file)
        for files in os.walk(path)
        for file in files[2]
    ]


def apply_lambda_image(image, fun):
    data = image.getdata()
    new_image = [fun(pixel) for pixel in data]
    image.putdata(new_image)
    del new_image[:]
    del data


def apply_lambda_image_filename(filename, fun):
    image = Image.open(filename).convert('RGBA')
    apply_lambda_image(image, fun)
    image.save(filename)
    del image


def apply_lambda_text(filename, fun):

    def replace_hex(match):
        r, g, b = hex2rgb(match.group(0))
        result = fun((r, g, b, None))
        return rgb2hex(result)

    def replace_rgba(match):
        r, g, b, a = match.groups()
        r, g, b = [int(x) for x in (r, g, b)]
        a = round(float(a) * 255)
        r, g, b, a = fun((r, g, b, a))
        a = a / 255
        return rgba2str((r, g, b, a))

    data = None
    with open(filename) as file:
        try:
            data = file.read()
        except Exception as e:
            print("\nerror while reading {f}:".format(f=filename))
            print(e)
        else:
            data = re.sub('#[0-9A-Fa-f]{6}',
                          replace_hex, data)
            data = re.sub("rgba\((\d+), (\d+), (\d+), ([-+]?\d*\.\d+|\d+)\)",
                          replace_rgba, data)
    if not data:
        return
    with open(filename, 'w') as file:
        file.write(data)
        file.flush()
        file.close()
    del data


def is_image_file(filename):
    filename = filename.lower()
    for ext in ('png', 'jpg'):
        if filename.endswith('.' + ext):
            return True
    return False


def progress_dot():
    sys.stdout.write('.')
    sys.stdout.flush()


function_cache = {}


def get_function(func_name):
    if func_name in function_cache:
        return function_cache[func_name]

    fun = getattr(presets, func_name, None)
    if not fun:
        print("preset '{}' not found".format(func_name))
        try:
            fun = eval(fun_name)
        except NameError as e:
            print(e)
            sys.exit(4)
        if not fun:
            print("'{}' is not a function".format(func_name))
            sys.exit(3)
    if len(inspect.getargspec(fun).args) == 4:
        def patched_fun(pixel):
            return fun(pixel[0], pixel[1], pixel[2], pixel[3])
        function_cache[func_name] = patched_fun
    else:
        function_cache[func_name] = fun
    return function_cache[func_name]


def apply_lambda(func_name, file_path):
    f = get_function(func_name)

    def patched_fun(pixel):
        """
        it looks so classy because of performance issues.
        """
        r, g, b, a = f(pixel)
        if r:
            if r < 0:
                r = 0
            elif r > 255:
                r = 255
        if g:
            if g < 0:
                g = 0
            elif g > 255:
                g = 255
        if b:
            if b < 0:
                b = 0
            elif b > 255:
                b = 255
        if a:
            if a < 0:
                a = 0
            elif a > 255:
                a = 255
        return r, g, b, a

    progress_dot()
    if is_image_file(file_path):
        apply_lambda_image_filename(file_path, patched_fun)
    else:
        apply_lambda_text(file_path, patched_fun),


def apply_dir(dir_path, func_name):
    files = ls_r(dir_path)
    print(len(files))
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    for file_path in files:
        pool.apply_async(apply_lambda, (func_name, file_path))
    pool.close()
    pool.join()
    print("")
