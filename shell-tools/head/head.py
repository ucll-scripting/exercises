#!/usr/bin/env python

import argparse
import sys


def create_parser():
    parser = argparse.ArgumentParser(prog='head')
    parser.add_argument('file', help='file', nargs='?')
    parser.add_argument('-n', '--lines', help='number of lines to print', action='store', default=5, type=int)
    return parser


def print_head(stream, n):
    for _ in range(n):
        print(stream.readline(), end='')


args = create_parser().parse_args()

if args.file:
    with open(args.file, 'r') as file:
        print_head(file, args.lines)
else:
    print_head(sys.stdin, args.lines)