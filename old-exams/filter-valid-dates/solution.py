from datetime import datetime
import sys


def is_valid(string):
    try:
        datetime.strptime(string, '%d-%m-%Y')
        return True
    except ValueError:
        return False

count = 0

with open('input.txt') as f:
    with open('output.txt', 'w') as out:
        for line in f:
            line = line.strip()
            if is_valid(line):
                print(line, file=out)
