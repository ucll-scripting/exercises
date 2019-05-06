#!/usr/bin/env python

import sys
import csv


table = {}
students_with_overlaps = set()

with open(sys.argv[1]) as file:
    data = csv.DictReader(file)

    for row in data:
        student = row['Student ID']
        date = row['Datum']
        part_of_day = row['Dagdeel']

        d = table.setdefault(student, {})

        key = (date, part_of_day)
        old_count = d.get(key, 0)
        new_count = old_count + 1
        d[key] = new_count

        if new_count == 2:
            students_with_overlaps.add(student)


for student in sorted(list(students_with_overlaps)):
    overlap_moments = sorted( when for when, count in table[student].items() if count > 1 )

    for when in overlap_moments:
        date, part_of_day = when
        count = table[student][when]
        print(f"{student} has {count} exams on {date} ({part_of_day})")

