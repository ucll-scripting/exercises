import re


def contains_no_a(string):
    return re.fullmatch(r'[^a]*', string)
