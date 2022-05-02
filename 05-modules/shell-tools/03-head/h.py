import sys

import argparse


parser = argparse.ArgumentParser(prog='lines')
parser.add_argument('file')
parser.add_argument('--lines','-n',type = int,default = 5)


args = parser.parse_args()


with open(args.file,'r') as f:
    for line in range(args.lines):
        print(f.readline(), end='')
     
