import re


def does_not_start_with_a(string):
    return re.fullmatch('|[^a].*', string)
