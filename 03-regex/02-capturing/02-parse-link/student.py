# Write your code here
import re
def parse_link(string):
    match = re.fullmatch(r'<a href="(.*)">(.*)</a>',string)
    if match:
        return tuple( [str(x) for x in match.groups()[::-1]])
    else:
        return None 