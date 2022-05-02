import csv

with open('input.csv') as f:
    reader = csv.DictReader(f)
    l = []
    d = dict()
    for row in reader:
        keys = list(row.keys())[1:]
        for i in keys:
            l.append((i,row[i]))
    for i,j in l:
        if j == 'yes':
            d[i] = d.get(i,0) + 1
    d = dict(sorted(d.items(),key=lambda x: x[1],reverse=True))
with open('output.txt','w') as o:
    for i,j in d.items():
        o.write(f"{i} {j}\n")
    