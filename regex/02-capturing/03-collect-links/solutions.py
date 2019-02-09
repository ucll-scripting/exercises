import re


def collect_links(string):
    return re.findall(r'<a href="(.*)">', string)

