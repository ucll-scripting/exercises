import re


def does_not_end_with_a(string):
    return re.fullmatch('|.*[^a]', string)
