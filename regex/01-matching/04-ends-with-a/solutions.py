import re


def ends_with_a(string):
    return re.search(r'a$', string)
