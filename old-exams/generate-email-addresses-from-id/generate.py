import random

random.seed(49188)


with open('input.txt', 'w') as out:
    for _ in range(10000):
        prefix = random.choice('rsuRSU')
        n = random.randint(0, 99999)
        id = f'{prefix}{str(n).rjust(7, "0")}'
        out.write(f'{id}\n')