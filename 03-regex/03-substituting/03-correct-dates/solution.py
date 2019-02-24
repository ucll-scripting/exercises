import re


def correct_dates(string):
    return re.sub(r'(\d+)/(\d+)/(\d+)', r'\2/\1/\3', string)