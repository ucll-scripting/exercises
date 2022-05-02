
import argparse

parser = argparse.ArgumentParser(prog='uniq')

parser.add_argument('filename',default='sys.stdin')
parser.add_argument('-i','--ignorecase',action='store_true')

args = parser.parse_args()

with open(args.filename, 'r') as f:
    if args.ignorecase:
        for line in f.readlines():
            