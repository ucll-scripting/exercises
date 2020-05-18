import random
import json


random.seed(37120)

ids = list(set( f'r{str(random.randint(0, 99999)).rjust(7, "0")}' for _ in range(1000) ))
ids.sort()
random.shuffle(ids)

def generate_student(id):
    avg = random.randint(5, 18)
    n = random.randint(5, 10)
    grades = [ min(20, avg + random.randint(-5, 5)) for _ in range(n) ]
    return { 'id': id, 'grades': grades }

def generate_students():
    return [ generate_student(id) for id in ids ]

with open('input.json', 'w') as out:
    students = generate_students()
    json.dump(students, out)