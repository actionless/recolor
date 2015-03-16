#!/bin/env python3

import sys
import inspect

from ireplace import apply_dir
import presets


def print_help():
    print('need help?')
    sys.exit(2)


def normalize_function_arguments(fun):
    if len(inspect.getargspec(fun).args) == 4:
        return lambda pixel: fun(pixel[0], pixel[1], pixel[2], pixel[3])
    else:
        return fun


def main():

    if len(sys.argv) < 3:
        print_help()
    path = sys.argv[1]
    fun_name = sys.argv[2]

    print(path)

    fun = getattr(presets, fun_name, None)
    if not fun:
        print("lambda '{}' not found".format(fun_name))
        fun = eval(fun_name)
        if not fun:
            print("'{}' is not a function".format(fun_name))
            sys.exit(3)
    fun = normalize_function_arguments(fun)

    apply_dir(path, fun)

if __name__ == '__main__':
    main()
