import sys
import re


def replace(old, new, filename):
    with open(filename, 'r') as file:
        contents = file.read()

    contents = re.sub(old, new, contents)

    with open(filename, 'w') as file:
        file.write(contents)


if len(sys.argv) != 4:
    print('Three parameters required')
else:
    old, new, filename = sys.argv[1:]
    replace(old, new, filename)
