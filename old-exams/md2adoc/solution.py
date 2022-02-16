import sys
import re


def fix_header(line):
    def replace(match):
        return "=" * len(match.group(1)) + match.group(2)
    return re.sub(r'^(#+)(.*)', replace, line)


def fix_bullet_point(line):
    def replace(match):
        indent = match.group(1)
        text = match.group(2)
        return "*" * (len(indent) // 2) + '*' + text
    return re.sub(r'^( *)\*(.*)', replace, line)


for line in sys.stdin:
    line = fix_header(line)
    line = fix_bullet_point(line)
    print(line, end='')
