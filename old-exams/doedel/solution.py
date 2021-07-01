from collections import Counter
import csv


counts = Counter()


with open('input.txt') as file:
    reader = csv.DictReader(file)
    for line in reader:
        for key in line.keys():
            if key != 'name' and line[key] == 'yes':
                counts[key] += 1

sorted_by_date = sorted(counts.items(), key=lambda p: p[1], reverse=True)

for date, votes in sorted_by_date:
    print(f'{date} {votes}')