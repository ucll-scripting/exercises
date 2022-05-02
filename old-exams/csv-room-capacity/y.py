from cmath import inf
import csv
from numpy import sort


with open("exam-schedule.csv") as csv_file:
    reader = csv.DictReader(csv_file)
    combinations = []
    for row in reader:
        combinations.append((row["Datum"],row["Dagdeel"],row["Lokaal"]))
    
    countdict = dict()
        
    for i in combinations:
        countdict[i] = countdict.get(i,0) + 1
    
    list = []
    for key,value in countdict.items():
        list.append((key[2],value))
    list.sort(key=lambda x: (x[0],x[1]))
    
    countdict2 = dict()
    for i,j in list:
        countdict2[i] = j

with open("output.txt",'w') as csv_file:
    for key,value in countdict2.items():
        csv_file.write(f"{key} {value}\n")
    
    
        
