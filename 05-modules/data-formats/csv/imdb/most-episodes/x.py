import csv
import sys


def second(xs):
    return xs[1]

table = {}
with open("C:\\Users\\Ninov\\Downloads\\title.episode.tsv\\data.tsv", encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter='\t', quoting=csv.QUOTE_NONE)
    for row in reader:
        id = row['parentTconst']
        if id not in table:
            table[id] = 0
        table[id] += 1
    
table = dict(sorted(table.items(), key=lambda item: item[1],reverse=True))

tvserie = next(iter(table))
print("Max episode count: " + str(table[tvserie]))
with open("C:\\Users\\Ninov\\Downloads\\title.basics.tsv\\data.tsv", encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter='\t', quoting=csv.QUOTE_NONE)
    for row in reader:
       if row['tconst'] == tvserie:
           print(row['originalTitle'])
           break
    
    
    