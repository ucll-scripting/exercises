import urllib.request
import sys


with urllib.request.urlopen(sys.argv[1]) as input:
    contents = input.read()
    print(contents)
