import argparse


parser = argparse.ArgumentParser(prog='thumbnail')
parser.add_argument('--size',default='64x64')
parser.add_argument('--pattern',default='%b-thumbnail%x')
parser.add_argument('files')

args = parser.parse_args()

print(args)




