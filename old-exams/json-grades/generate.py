import random
import json


random.seed(37119)

def generate_student():
    id = f'r{str(random.randint(0, 99999)).rjust(7, "0")}'
    avg = random.randint(5, 18)
    n = random.randint(5, 10)
    grades = [ min(20, avg + random.randint(-5, 5)) for _ in range(n) ]
    return { 'id': id, 'grades': grades }

def generate_students():
    return [ generate_student() for _ in range(100) ]

with open('input.json', 'w') as out:
    students = generate_students()
    json.dump(students, out)