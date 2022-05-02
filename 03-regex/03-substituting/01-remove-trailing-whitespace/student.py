import re


def remove_trailing_whitespace(string):
    match = re.sub(r'\s+$','', string,flags=re.MULTILINE)
    return match