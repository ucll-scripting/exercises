import re


def three_digits(string):
    return re.fullmatch(r'\d{3}', string)
