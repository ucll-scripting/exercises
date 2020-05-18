import random


random.seed(8081)


def generate_time():
    n = random.randint(3, 5)
    h = str(random.randint(0, 30)).rjust(2, '0')
    m = str(random.randint(0, 70)).rjust(2, '0')
    s = str(random.randint(0, 70)).rjust(2, '0')
    return ":".join( [ h, m, s ] )

def generate_crap():
    return "".join( random.choice('abcdefghijklmnopqrstuvwxyz123456789.') for _ in range(random.randint(10, 50)) )

def generate_line():
    return " ".join( random.choice([generate_time, generate_crap])() for _ in range(random.randint(2, 10)) )

with open('input.txt', 'w') as out:
    for _ in range(1000):
        out.write(generate_line() + "\n")