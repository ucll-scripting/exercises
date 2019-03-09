import urllib.request
import sys


word = sys.argv[1]

with urllib.request.urlopen(f"https://www.dictionary.com/browse/{word}") as input:
    contents = input.read()
    print(contents)