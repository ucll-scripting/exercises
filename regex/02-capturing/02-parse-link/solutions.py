import re


def parse_link(string):
    match = re.fullmatch(r'<a href="(.*)">(.*)</a>', string)
    if match:
        url, caption = match.groups()
        return (caption, url)
    else:
        return None
