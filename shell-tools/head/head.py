#!/usr/bin/env python

import argparse
import sys


def create_parser():
    parser = argparse.ArgumentParser(prog='head')
    parser.add_argument('file', help='file')
    parser.add_argument('-n', '--lines', help='number of lines to print', action='store', default=5, type=int)
    return parser

args = create_parser().parse_args()

with open(args.file, 'r') as file:
    for _ in range(args.lines):
        print(file.readline(), end='')