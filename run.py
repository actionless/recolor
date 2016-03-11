#!/bin/env python

import argparse
import shutil

from ireplace import apply_dir


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

    func_name = args.fun_name
    path = args.dest

    if args.src:
        try:
            shutil.rmtree(path)
        # except FileNotFoundError:
        except (IOError, OSError):
            pass
        shutil.copytree(args.src, path)

    print(path)
    apply_dir(path, func_name)

if __name__ == '__main__':
    main()
