import sys
import re


def remove_comments(filename):
    with open(filename, 'r') as file:
        contents = file.read()

    contents = re.sub('#.*$', '', contents, flags=re.MULTILINE)

    with open(filename, 'w') as file:
        file.write(contents)


for file in sys.argv[1:]:
    remove_comments(file)