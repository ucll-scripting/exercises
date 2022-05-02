import json
import sys
import csv


reader = csv.reader(sys.stdin)
linecount = 0
list = []
for row in reader:
    if linecount == 0:
        headers = row
        linecount +=1
    else:
        list.append({headers[0]:row[0],headers[1]:row[1],headers[2]:row[2]})
        
print(json.dumps((list)))