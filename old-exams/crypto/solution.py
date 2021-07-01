import json
import sys


data = json.load(sys.stdin)

for coin in data:
    currency = coin['currency']
    history = coin['history']
    lowest = min(history)
    highest = max(history)
    current = history[-1]
    print(f'{currency} {lowest} {highest} {current}')