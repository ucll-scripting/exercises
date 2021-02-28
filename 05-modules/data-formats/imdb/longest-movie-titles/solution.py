import csv
import sys


with open('../title-basics.tsv', encoding="utf-8") as file:
    reader = csv.DictReader(file, delimiter='\t')
    top = sorted((row['originalTitle'] for row in reader), reverse=True, key=len)[0:100]

print("\n".join(top))
