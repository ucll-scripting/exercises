import re


def only_digits(string):
    return re.fullmatch(r'[0123456789]*', string)
