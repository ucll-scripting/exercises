import sys

filenames = sys.argv[1:]

for i in filenames:
    with open(i, 'r') as f:
        for line in f:
            print(line, end='')
    
