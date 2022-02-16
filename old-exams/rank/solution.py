import json
import sys


def name(entry):
    return entry['name']

def score(entry):
    return entry['score']


data = json.load(sys.stdin)

data.sort(key=score, reverse=True)

for index, entry in enumerate(data):
    rank = index + 1
    print(f'{rank} {name(entry)}')
