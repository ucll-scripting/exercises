import sys
import re


data = sys.stdin.read()

def evaluate(match):
    return str(eval(match.group(1).strip()))

print(re.sub(r'\$\{(.*?)\}', evaluate, data), end='')