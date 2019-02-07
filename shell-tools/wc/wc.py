import argparse
import sys
import re
import os


def _line_count(filename):
    with open(filename, 'r') as file:
        return len(file.readlines())

def _word_count(filename):
    with open(filename, 'r') as file:
        return len(re.split(r'\s+', file.read()))

def _byte_count(filename):
    return os.path.getsize(filename)

def _char_count(filename):
    with open(filename, 'r') as file:
        return len(file.read())


def process_command_line_arguments():
    parser = argparse.ArgumentParser(prog='wc')
    parser.add_argument('files', help='print line count', nargs='+')
    parser.add_argument('-l', '--lines', help='print line count', dest='counters', action='append_const', const=_line_count)
    parser.add_argument('-c', '--bytes', help='print byte counts', dest='counters', action='append_const', const=_byte_count)
    parser.add_argument('-m', '--chars', help='print character counts', dest='counters', action='append_const', const=_char_count)
    parser.add_argument('-w', '--words', help='print word counts', dest='counters', action='append_const', const=_word_count)

    args = parser.parse_args()

    counters = args.counters or [ _line_count, _word_count, _byte_count ]
    files = args.files

    data = [ (*[ c(f) for c in counters ], f) for f in files ]

    if len(data) > 1:
        data.append(tuple((*tuple( sum(t[i] for t in data) for i in range(len(counters)) ), 'total')))

    string_data = [ tuple( str(x) for x in row) for row in data ]
    column_widths = [ max( len(row[i]) for row in string_data ) for i in range(len(string_data[0])) ]

    for row in string_data:
        print(" ".join( row[i].rjust(column_widths[i]) for i in range(len(row)) ))


process_command_line_arguments()