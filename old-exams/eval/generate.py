import random
import string

rnd = random.Random(314541)


def random_whitespace():
    return " " * rnd.randint(0, 1)


def random_operation():
    left = rnd.randint(2, 999999)
    right = rnd.randint(2, 999999)
    op = rnd.choice('+*')
    return f'{left}{random_whitespace()}{op}{random_whitespace()}{right}'



def random_paragraph():
    result = ''
    while len(result) < 1000:
        result += ''.join(rnd.choices([*string.ascii_lowercase, '     '], k=rnd.randint(2, 10)))
        result += ' '
        result += "${" + random_whitespace() + random_operation() + random_whitespace() + "}"
        result += ' '
    return result.strip()


with open('input.txt', 'w') as f:
    for _ in range(1000):
        print(random_paragraph(), file=f)
