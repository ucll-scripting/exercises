import re

def valid_time(h, m, s):
    return 0 <= int(h) <= 23 and 0 <= int(m) < 60 and 0 <= int(s) < 60

with open('input.txt') as file:
    with open('output.txt', 'w') as out:
        line_index = 0

        for line in file:
            line_index += 1
            for match in [ match for match in re.findall(r'(\d{1,2}):(\d{1,2}):(\d{1,2})', line) if not valid_time(*match) ]:
                print(f'{line_index} {":".join(match)}', file=out)


