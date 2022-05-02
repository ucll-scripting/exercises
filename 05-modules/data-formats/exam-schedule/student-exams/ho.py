import sys
import csv
import argparse


parser = argparse.ArgumentParser(prog='format')

parser.add_argument('path', default='.')
parser.add_argument('studentName')
parser.add_argument('-f','--format', help='format for output info', default='%d %c')


def derive_format(pattern, row):
    date = str(row["Datum"])
    partofday = str(row["Dagdeel"])
    course = str(row["OLA Naam"])
    location = str(row["Lokaal"])
    hour = str(row["Startuur"])
   
    return pattern.replace('%d', date).replace('%p', partofday).replace('%t', hour).replace('%c', course).replace('%l',location)

args = parser.parse_args()
pattern = args.format
with open(args.path,encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter=',')
    #!! Datum 28-08-18 Student ID OLA Naam
    
    student = args.studentName
    a = set()
    
    for row in reader:
        naam = row["Student ID"]
        
        if naam == student:
            print(derive_format(args.format,row))
            
        

    














