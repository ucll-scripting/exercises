import re


def only_digits(string):
    return re.fullmatch('[0123456789]*', string)
