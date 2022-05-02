import sys

files = sys.argv[1:]
for i in files:
    with open(i, 'r') as fileread:
        lines = fileread.readlines()
    with open(i, 'w') as filewrite:
        for line in lines:
            if not line.startswith('#'):
                filewrite.write(line)
            
                

