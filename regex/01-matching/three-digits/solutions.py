import re


def three_digits(string):
    return re.fullmatch('\d{3}', string)
