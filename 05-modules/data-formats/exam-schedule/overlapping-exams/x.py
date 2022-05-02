import sys
import csv
import itertools
import json
from pprint import pprint




with open("C:\\Users\\Ninov\\Desktop\\scipting\\05-modules\\data-formats\\exam-schedule\\exam-schedule.csv", encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter=',')
    #!! Datum Dagdeel  28-08-18  vm nm ''
    a = {}
    dagdelen = {
        "vm" :"morning",
        "nm" :"afternoon",
        "av" :"evening",
        ""   :"?"
        }
    for row in reader:
        naam = row["Student ID"]
        datum = row["Datum"]
        dagdeel = dagdelen[row["Dagdeel"]]
        
        if (naam,datum,dagdeel) in a:
            a[(naam,datum,dagdeel)] += 1
        else:
            a[(naam,datum,dagdeel)] = 1
    a = dict(sorted([(i,j) for i,j in a.items() if j > 1]))
    
    [print(f"{naam} has {number} exams on {datum} ({dagdeel})") for (naam,datum,dagdeel),number in a.items()]
   

