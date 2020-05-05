import random


random.seed(89131)


def generate_hex():
    n = random.randint(1, 2**32)
    return f"$HEX({n})"

def generate_crap():
    return "".join( random.choice('abcdefghijklmnopqrstuvwxyz123456789.:') for _ in range(random.randint(10, 50)) )

def generate_line():
    return " ".join( random.choice([generate_hex, generate_crap])() for _ in range(random.randint(2, 10)) )

with open('input.txt', 'w') as out:
    for _ in range(10000):
        out.write(generate_line() + "\n")