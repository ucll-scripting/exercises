import argparse
import sys
import re
import os


def line_count(filename):
    with open(filename, 'r') as file:
        return len(file.readlines())


def word_count(filename):
    with open(filename, 'r') as file:
        return len(re.split(r'\s+', file.read()))


def byte_count(filename):
    return os.path.getsize(filename)


def char_count(filename):
    with open(filename, 'r') as file:
        return len(file.read())


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

    parser.add_argument('files', help='print line count', nargs='+')
    parser.add_argument('-l', '--lines', help='print line count', dest='counters', action='append_const', const=line_count)
    parser.add_argument('-c', '--bytes', help='print byte counts', dest='counters', action='append_const', const=byte_count)
    parser.add_argument('-m', '--chars', help='print character counts', dest='counters', action='append_const', const=char_count)
    parser.add_argument('-w', '--words', help='print word counts', dest='counters', action='append_const', const=word_count)

    return parser


def collect_data(files, counters):
    def process_file(file):
        return (*( counter(file) for counter in counters ), file)

    return [ process_file(f) for f in files ]


def add_total_row(table):
    if len(table) > 1:
        n_columns = len(table[0])
        sums = ( sum(t[i] for t in table) for i in range(n_columns - 1) )
        table.append(tuple( [ *sums, 'total' ]))


def convert_to_strings(table):
    return [ tuple(str(x) for x in row) for row in table ]


def main():
    args = create_parser().parse_args()

    # If no counters were specified, use defaults
    counters = args.counters or [ line_count, word_count, byte_count ]
    files = args.files

    # Collect counts for each file
    table = collect_data(files, counters)

    # Add total row if necessary
    add_total_row(table)

    # Convert all data to strings
    string_table = convert_to_strings(table)

    # Print table
    print_table(string_table)


main()