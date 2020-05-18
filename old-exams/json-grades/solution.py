import json


def average(ns):
    return sum(ns) / len(ns)


with open('input.json') as f:
    students = json.load(f)

result = {}

for student in students:
    id = student['id']
    grades = student['grades']
    result[id] = average(grades)

with open('output.txt', 'w') as out:
    for student, avg in sorted(result.items(), key=lambda p: p[0]):
        out.write(f'{student} {round(avg)}\n')