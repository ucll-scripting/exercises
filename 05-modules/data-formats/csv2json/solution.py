import json
import csv
import sys


data = list(csv.DictReader(sys.stdin))

print(json.dumps(data))