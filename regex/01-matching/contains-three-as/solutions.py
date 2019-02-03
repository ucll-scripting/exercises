import re


def contains_three_as(string):
    return re.search('a.*a.*a', string)
