import argparse
import sys
import re

parser = argparse.ArgumentParser(prog='loc')
parser.add_argument('-e' '--count-empty-lines', help='Counts empty lines', dest='count_empty_lines', action='store_true')
parser.add_argument('--comment', help='Comment identifier')

args = parser.parse_args()


skip_regexes = []

if not args.count_empty_lines:
    skip_regexes.append(r'^\s*$')

if args.comment:
    skip_regexes.append(f'^\\s*{args.comment}')


count = 0

for line in sys.stdin:
    if not any(re.match(skip_regex, line) for skip_regex in skip_regexes):
        count += 1

print(count)