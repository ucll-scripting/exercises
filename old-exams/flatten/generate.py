import random


random.seed(95991)

def generate_student():
    n = random.randint(0, 99999)
    prefix = random.choice('rs')
    return f'{prefix}{str(n).rjust(7, "0")}'

students = list(set(generate_student() for _ in range(100000)))
students.sort()
random.shuffle(students)

with open('input.txt', 'w') as out:
    for _ in range(1000):
        n = random.randint(1, 20)
        out.write(",".join(generate_student() for _ in range(n)))
        out.write("\n")
