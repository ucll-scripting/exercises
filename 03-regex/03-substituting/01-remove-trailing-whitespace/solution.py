import re


def remove_trailing_whitespace(string):
    return re.sub('\s+$', '', string, flags=re.MULTILINE)
