import random


random.seed(94881)

with open('input.txt', 'w') as out:
    for _ in range(1000):
        print(random.randint(0, 999999999), file=out)
