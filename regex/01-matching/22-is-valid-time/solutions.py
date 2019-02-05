import re


def is_valid_email_address(string):
    return re.fullmatch('[a-z0-9.]+@(student\.)?ucll\.be', string)