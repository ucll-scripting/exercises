import re


def abc_or_xyz(string):
    return re.fullmatch(r'abc|xyz', string)
