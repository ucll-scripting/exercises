#!/usr/bin/env python
import argparse
import sys
import re
import os


def case_sensitive_comparison(x, y):
    return x == y


def case_insensitive_comparison(x, y):
    return x.lower() == y.lower()


def create_parser():
    parser = argparse.ArgumentParser(prog='uniq')

    parser.add_argument('file', help='file', nargs='?')
    parser.add_argument('-i', '--ignore-case', dest='comparer', action='store_const', const=case_insensitive_comparison)
    parser.set_defaults(comparer=case_sensitive_comparison)

    return parser


def uniq(stream, comparer):
    last_line = None

    for line in stream:
        if not last_line or not comparer(last_line, line):
            print(line, end='')
            last_line = line



def main():
    args = create_parser().parse_args()
    file = args.file
    args = { 'comparer': args.comparer }

    if file:
        with open(file, 'r') as stream:
            uniq(stream, **args)
    else:
        uniq(sys.stdin, **args)


main()