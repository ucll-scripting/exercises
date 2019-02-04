import re


def ten_times_abc(string):
    return re.fullmatch(r'(abc){10}', string)
