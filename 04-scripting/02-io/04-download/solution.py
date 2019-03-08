import urllib.request
import sys


with urllib.request.urlopen(sys.argv[1]) as input:
    print(input.read())