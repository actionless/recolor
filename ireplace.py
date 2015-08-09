import os
import re
import sys
import multiprocessing
import pickle

import dill
from PIL import Image


R = 0
G = 1
B = 2
A = 3


def rgb2hex(pixel):
    """ convert an (R, G, B) tuple to #RRGGBB """
    r, g, b, a = pixel
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)


def hex2rgb(colorstring):
    """ convert #RRGGBB to an (R, G, B) tuple """
    colorstring = colorstring.strip()
    if colorstring[0] == '#':
        colorstring = colorstring[1:]
    if len(colorstring) != 6:
        raise(ValueError("input #%s is not in #RRGGBB format" % colorstring))
    r, g, b = colorstring[:2], colorstring[2:4], colorstring[4:]
    r, g, b = [int(n, 16) for n in (r, g, b)]
    return r, g, b


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


def apply_lambda_image(filename, fun):
    image = Image.open(filename).convert('RGBA')
    data = image.getdata()
    new_image = [fun(pixel) for pixel in data]
    image.putdata(new_image)
    image.save(filename)
    del image
    del new_image[:]
    del data


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
        except:
            print("error or reading {f}".format(f=filename))
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


def apply_lambda(args):
    f, file_path = args
    if isinstance(f, bytes):
        f = dill.loads(f)

    def patched_fun(pixel):
        """
        it looks so classy because of performance issues.
        it takes 1.7 seconds on testsuite
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

    def patched_fun_bak(pixel):
        """
        this one takes 3 seconds on the same testsuite :(
        """
        return tuple(
            x if x and 0 < x < 255 else x for x in f(pixel)
        )

    progress_dot()
    if is_image_file(file_path):
        apply_lambda_image(file_path, patched_fun)
    else:
        apply_lambda_text(file_path, patched_fun),


def apply_dir(dir_path, fun):
    try:
        pickle.dumps(fun)
    except pickle.PicklingError:
        fun = dill.dumps(fun)
    files = ls_r(dir_path)
    print(len(files))
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    pool.map(apply_lambda, ((fun, file_path) for file_path in files))
    print()
