import sys


for filename in sys.argv[1:]:
    with open(filename, 'r') as file:
        for line in file:
            print(line, end='')