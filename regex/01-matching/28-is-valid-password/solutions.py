import re


def is_valid_password(string):
    positive_regexes = [
        r'.{8,}',
        r'[0-9]',
        r'[a-z]',
        r'[A-Z]',
        r'[-+/.*@]',
    ]

    negative_regexes = [
        r'(.)\1{2}',
        r'(.)(.*\1){3}'
    ]

    return all(re.search(regex, string) for regex in positive_regexes) and not any(re.search(regex, string) for regex in negative_regexes)