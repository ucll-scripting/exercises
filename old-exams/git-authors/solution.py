import re

authors = set()

with open('input.txt') as f:
    for line in f:
        m = re.search(r'Author: (.*) <', line)
        if m:
            authors.add(m.group(1))

with open('output.txt', 'w') as out:
    out.write("\n".join(sorted(list(authors))))