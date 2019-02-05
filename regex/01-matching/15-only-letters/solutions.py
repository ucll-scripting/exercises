import re


def only_letters(string):
    return re.fullmatch(r'[a-zA-Z]*', string)
