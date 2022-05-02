import sys
import argparse


parser = argparse.ArgumentParser(prog='lineslast')
parser.add_argument('file')
parser.add_argument('--lines','-n',type = int,default = 5)


args = parser.parse_args()


with open(args.file,'r') as f:
    lines = f.readlines()
    for line in lines[-args.lines:]:
        print(line,end='')

     
