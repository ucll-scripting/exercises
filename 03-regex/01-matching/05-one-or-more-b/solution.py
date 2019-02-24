import re


def one_or_more_b(string):
    return re.fullmatch('b+', string)
