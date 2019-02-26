import re


def abc_or_xyz(string):
    return re.fullmatch('abc|xyz', string)
