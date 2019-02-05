import re


def ends_with_a(string):
    return re.search('a$', string)
