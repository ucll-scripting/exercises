import sys
import csv
import itertools
import json



def second(xs):
    return xs[1]

with open("C:\\Users\\Ninov\\Desktop\\scipting\\05-modules\\data-formats\\exam-schedule\\exam-schedule.csv", encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter=',')

    a = {}
    for row in reader:
        naam = row["Student ID"]
        if naam in a:
            a[naam] += 1
        else:
            a[naam] = 1

    sort_a = dict(sorted(a.items(), key=lambda x: x[1], reverse=True))
    
    
    top_10 = dict(itertools.islice(sort_a.items(),10))

    for key,value in top_10.items():
        print(f"{str(key).ljust(15)} {str(value)}")


