from zipfile import ZipFile, BadZipFile
from itertools import product
import string
import sys


filename = 'crack.zip'
alphabet = string.ascii_lowercase

with ZipFile(filename) as zip:
    for password in ("".join(combination) for combination in product(alphabet, repeat=4)):
        print(f'Trying #{password}')
        pwd = bytes(password, 'ascii')
        try:
            bs = zip.read('file.txt', pwd=pwd)
            print(f"Found password! {password}")
            string = bs.decode('utf-8')
            print(string)
            sys.exit(0)
        except RuntimeError as e:
            pass
        except BadZipFile:
            pass

print('Failed to find password')