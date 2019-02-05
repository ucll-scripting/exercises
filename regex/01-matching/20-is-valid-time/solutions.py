import re


def is_valid_time(string):
    return re.fullmatch('[0-9]{2}:[0-9]{2}:[0-9]{2}(\.[0-9]{3})?', string)