#!/usr/bin/env python

import argparse
import sys
import csv


parser = argparse.ArgumentParser()
parser.add_argument('filename', help='.csv file to consult')
parser.add_argument('id', help='student id')
parser.add_argument('--format', help='format string', default='%d %c')
args = parser.parse_args()


with open(args.filename) as file:
    data = csv.DictReader(file)

    for row in data:
        student_id = row['Student ID']

        if student_id == args.id:
            date = row['Datum']
            part_of_day = row['Dagdeel']
            course = row['OLA Naam']
            location = row['Lokaal']
            hour = row['Startuur']

            output = args.format
            output = output.replace('%d', date)
            output = output.replace('%p', part_of_day)
            output = output.replace('%c', course)
            output = output.replace('%l', location)
            output = output.replace('%h', hour)

            print(output)
