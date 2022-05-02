import argparse
from zipfile import ZipFile
import os

def makeparser():
    parser = argparse.ArgumentParser(prog="list-files")
    parser.add_argument("file",help="Filename")
    return parser
    
args = makeparser().parse_args()




filename = args.file

with ZipFile(filename) as zip:
    for name in zip.namelist():
        print(name)
