import json
import sys
from collections import Counter
import calendar


data = json.load(sys.stdin)

counter = Counter([person['birthday']['month'] for person in data])

for i in range(1, 12 + 1):
    month = calendar.month_name[i].rjust(10, ' ')
    freq = counter[i]
    print(f'{month} {"*" * freq}')
