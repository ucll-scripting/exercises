import random


rnd = random.Random(39119)


def generate_student():
    n = rnd.randint(0, 99999)
    prefix = rnd.choice('rs')
    return f'{prefix}{str(n).rjust(7, "0")}'

students = list(set(generate_student() for _ in range(100000)))
students.sort()
rnd.shuffle(students)

with open('all.txt', 'w') as out:
    for student in students:
        if rnd.randint(1, 10) <= 5:
            student = student.upper()
        out.write(f'{student}\n')

with open('attending.txt', 'w') as out:
    for student in students:
        if rnd.randint(1, 10) <= 6:
            if rnd.randint(1, 10) <= 5:
                student = student.upper()
            out.write(f'{student}\n')

