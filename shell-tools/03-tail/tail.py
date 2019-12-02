#!/usr/bin/env python

import argparse
import sys


def create_parser():
    parser = argparse.ArgumentParser(prog='tail')
    parser.add_argument('file', help='file', nargs='?')
    parser.add_argument('-n', '--lines', help='number of lines to print', action='store', default=5, type=int)
    return parser


def print_tail(stream, n):
    lines = stream.readlines()
    for line in lines[-n:]:
        print(line, end="")

args = create_parser().parse_args()

if args.file:
    with open(args.file, 'r') as file:
        print_tail(file, args.lines)
else:
    print_tail(sys.stdin, args.lines)
