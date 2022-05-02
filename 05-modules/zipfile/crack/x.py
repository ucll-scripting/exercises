#!/usr/bin/env python

from zipfile import ZipFile
from datetime import datetime
import argparse
import sys
import os
import zipfile
import string
import itertools
from numpy import byte
import time

start = time.time()



def generate_strings(length=4):
    chars = string.ascii_lowercase
    # "abcdefghijklmnopqrstuvwxyz"
    for item in itertools.product(chars, repeat=length):
        yield "".join(item)



string_pwd = "abcd"
byte_pwd = bytes(string_pwd,encoding='ascii')


with ZipFile("crack.zip", 'r') as thezip:
    for i in generate_strings() :
        try:
            bs = thezip.read('file.txt', pwd=bytes(i,encoding='ascii'))
            print(f"Found password: {i}")
            print(bs.decode('utf-8'))
            sys.exit(0)
        except RuntimeError as e:
            pass
        except zipfile.BadZipFile:
            pass

    # with thezip.open('crack.txt',mode='r') as thefile:
    #     string_pwd = "abcd"
    #     byte_pwd = bytes(string_pwd,encoding='ascii')
    #     print(byte_pwd)
    #     #Let us verify the operation..
    #     print(thefile.read())
    

