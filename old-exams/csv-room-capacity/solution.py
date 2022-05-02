import csv
import sys


result = {}

with open('exam-schedule.csv') as file:
    data = csv.DictReader(file)

    for row in data:
        location = row['Lokaal'].strip()
        date = row['Datum'].strip()
        daypart = row['Dagdeel'].strip()

        if not location or not date or not daypart:
            print(f'Error in row {row}')
            sys.exit(-1)
        # loctable = result.setdefault(location, {})
        # key = (date, daypart)
        # loctable[key] = loctable.get((date, daypart), 0) + 1
        result.setdefault(location, {})[(date, daypart)] = result.setdefault(location, {}).get((date, daypart), 0) + 1
    
locations = sorted(result.keys())
print(result['D1.14'])

with open('output.txt', 'w') as out:
    for location in locations:
        table = result[location]
        cap = max(table.values())
        out.write(f'{location} {cap}\n')

