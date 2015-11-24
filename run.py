#!/bin/env python3

import sys
import inspect
import argparse
import shutil

from ireplace import apply_dir
import presets


def normalize_function_arguments(fun):
    if len(inspect.getargspec(fun).args) == 4:
        return lambda pixel: fun(pixel[0], pixel[1], pixel[2], pixel[3])
    else:
        return fun


def main():

    parser = argparse.ArgumentParser(
        description='Apply color transformations to files in a folder.'
    )
    parser.add_argument('--src', dest='src',
                        # metavar='~/.themes/original-theme',
                        metavar='PATH_TO_ORIGINAL_THEME',
                        help='path to source theme to copy')
    parser.add_argument('dest',
                        # metavar='~/.themes/destination-theme',
                        metavar='PATH_TO_DESTINATION_THEME',
                        help='path to destionation theme to replace colors')
    parser.add_argument('fun_name',
                        # metavar='lambda r, g, b, a: (r+10, g-10, b, a)',
                        metavar='FUNCTION_TO_APPLY',
                        help='transformation preset or lambda to apply')
    args = parser.parse_args()

    path = args.dest
    fun_name = args.fun_name

    if args.src:
        shutil.rmtree(path)
        shutil.copytree(args.src, path)

    fun = getattr(presets, fun_name, None)
    if not fun:
        print("lambda '{}' not found".format(fun_name))
        fun = eval(fun_name)
        if not fun:
            print("'{}' is not a function".format(fun_name))
            sys.exit(3)
    fun = normalize_function_arguments(fun)

    print(path)
    apply_dir(path, fun)

if __name__ == '__main__':
    main()
