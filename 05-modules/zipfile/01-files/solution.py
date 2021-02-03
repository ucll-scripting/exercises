from zipfile import ZipFile
import sys


filename = sys.argv[1]

with ZipFile(filename) as zip:
    for name in zip.namelist():
        print(name)
