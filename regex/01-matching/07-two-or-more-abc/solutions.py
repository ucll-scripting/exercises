import re


def two_or_more_abc(string):
    return re.fullmatch('abc(abc)+', string)
