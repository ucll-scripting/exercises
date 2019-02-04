import re


def equals_abc(string):
    return re.fullmatch(r'abc', string)
