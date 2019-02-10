import re


def remove_trailing_whitespace(string):
    return re.sub(' +$', '', string, flags=re.MULTILINE)