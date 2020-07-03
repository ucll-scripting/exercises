import random

rnd = random.Random(56311)

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def generate_random_word():
    return "".join( rnd.choice(ALPHABET) for _ in range(rnd.randint(3, 10)) )

def generate_random_string():
    return " ".join( generate_random_word() for _ in range(100000) )

with open('input.txt', 'w') as file:
    print(generate_random_string(), file=file)
