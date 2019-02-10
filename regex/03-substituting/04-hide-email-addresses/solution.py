import re


def hide_email_addresses(string):
    def replace(match):
        return '*' * len(match.group(0))

    return re.sub(r'[a-zA-Z0-9.]+@[a-zA-Z0-9.]+', replace, string)

