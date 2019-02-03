import re


def three_letters(string):
    return re.fullmatch('[a-zA-Z]{3}', string)
