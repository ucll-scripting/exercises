#!/usr/bin/env python

import argparse
import sys
import re
import os


def line_count(data):
    return len(data.splitlines())


def word_count(data):
    return len(re.split(r'\s+', data))


def char_count(data):
    return len(data)


def print_table(table):
    def column(i):
        return (row[i] for row in table)

    def column_width(i):
        return max( len(cell) for cell in column(i) )

    n_columns = len(table[0])
    column_widths = [ column_width(i) for i in range(n_columns) ]

    def format_row(row):
        def format_cell(i):
            return row[i].rjust(column_widths[i])

        return " ".join( format_cell(i) for i in range(len(row)) )

    for row in table:
        print(format_row(row))


def create_parser():
    parser = argparse.ArgumentParser(prog='wc')

    parser.add_argument('files', help='files', nargs='*')
    parser.add_argument('-l', '--lines', help='print line count', dest='counters', action='append_const', const=line_count)
    parser.add_argument('-m', '--chars', help='print character counts', dest='counters', action='append_const', const=char_count)
    parser.add_argument('-w', '--words', help='print word counts', dest='counters', action='append_const', const=word_count)
    parser.set_defaults(counters = [ line_count, word_count, char_count ])

    return parser


def collect_data(filenames, counters):
    if filenames:
        def process_file(filename):
            with open(filename) as file:
                file_contents = file.read()
                return (*( counter(file_contents) for counter in counters ), filename)

        return [ process_file(filename) for filename in filenames ]
    else:
        data = sys.stdin.read()
        return [ tuple([ counter(data) for counter in counters ]) ]


def add_total_row(table):
    if len(table) > 1:
        n_columns = len(table[0])
        sums = ( sum(t[i] for t in table) for i in range(n_columns - 1) )
        table.append(tuple( [ *sums, 'total' ]))


def convert_to_strings(table):
    return [ tuple(str(x) for x in row) for row in table ]


def main():
    args = create_parser().parse_args()

    files = args.files

    # Collect counts for each file
    table = collect_data(files, args.counters)

    # Add total row if necessary
    add_total_row(table)

    # Convert all data to strings
    string_table = convert_to_strings(table)

    # Print table
    print_table(string_table)


main()