import datetime
import sys
import re

def by_date(s):
    m = re.search(r'Date:   (.*)', s)
    if not m:
        print(f'Could not find date in \n{s}')
        sys.exit(-1)
    date = m.group(1)
    return datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')

with open('input.txt') as f:
    input = f.read()

commits = re.findall(r'commit.*?Closed \#\d+', input, re.DOTALL | re.MULTILINE)

commits.sort(key=by_date, reverse=True)

with open('output.txt', 'w') as out:
    out.write("\n\n".join(commits))
