#!/usr/bin/env python
import argparse
import sys
import re
import os


def create_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument('file', help='file', nargs='?')
    parser.add_argument('-i', '--ignore-case', dest='case_sensitive', action='store_false')

    return parser


def equal_lines(line1, line2, case_sensitive):
    if not case_sensitive:
        line1 = line1.lower()
        line2 = line2.lower()
    return line1 == line2


def uniq(stream, case_sensitive):
    last_line = None

    for line in stream:
        if not last_line or not equal_lines(last_line, line, case_sensitive):
            print(line, end='')
            last_line = line


def main():
    args = create_parser().parse_args()
    file = args.file

    if file:
        with open(file, 'r') as stream:
            uniq(stream, args.case_sensitive)
    else:
        uniq(sys.stdin, args.case_sensitive)


main()