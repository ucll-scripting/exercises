#!/usr/bin/env python

from zipfile import ZipFile
from datetime import datetime
import argparse
import sys
import os


parser = argparse.ArgumentParser()
parser.add_argument('ziplocation')
parser.add_argument('root')
args = parser.parse_args()

now = datetime.now()
filename = os.path.join(args.ziplocation, now.strftime("%Y-%m-%d.zip"))
root = os.path.abspath(args.root)

with ZipFile(filename, 'w') as zip:
    for directory, subdirs, files in os.walk(root):
        for file in files:
            absolute_path = os.path.abspath(os.path.join(directory, file))
            relative_path = os.path.relpath(absolute_path, root)
            print(f"Adding {relative_path}")
            zip.write(absolute_path, arcname=relative_path)
