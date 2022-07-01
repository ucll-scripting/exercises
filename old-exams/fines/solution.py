import csv
import sys


result = {}

reader = csv.DictReader(sys.stdin)
for row in reader:
    plate = row['license_plate']
    speed = int(row['speed'])
    fine = speed - 120
    result[plate] = result.get(plate, 0) + fine


result = list(result.items())
result.sort(key=lambda p: (p[1], p[0]))

for key, value in result:
    print(f'{key} {value}')