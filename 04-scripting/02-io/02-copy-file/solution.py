import sys


with open(sys.argv[1], 'r') as input:
    with open(sys.argv[2], 'w') as output:
        output.write(input.read())