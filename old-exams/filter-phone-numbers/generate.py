import random

random.seed(851151)

c = 0

def random_phone_number():
    country = random.choice(['+32-', '0'])
    prefix = "4" + str(random.randint(5, 9)) + str(random.randint(0, 9))
    id = "-".join( str(random.randint(0, 99)).rjust(2, '0') for _ in range(3) )
    global c
    c += 1
    return f"{country}{prefix}-{id}"

def random_crap():
    def wrong_country():
        country = random.choice(['+31-', '+32', '+0'])
        prefix = "4" + str(random.randint(5, 9)) + str(random.randint(0, 9))
        id = "-".join( str(random.randint(0, 99)).rjust(2, '0') for _ in range(3) )
        return f"{country}{prefix}-{id}"

    def wrong_prefix():
        country = random.choice(['+32-', '0'])
        prefix = random.choice("012356789") + str(random.randint(1, 4)) + str(random.randint(0, 9))
        id = "-".join( str(random.randint(0, 99)).rjust(2, '0') for _ in range(3) )
        return f"{country}{prefix}-{id}"

    def wrong_id_size():
        country = random.choice(['+32-', '0'])
        prefix = "4" + str(random.randint(5, 9)) + str(random.randint(0, 9))
        id = "-".join( str(random.randint(0, 99)).rjust(2, '0') for _ in range(4) )
        return f"{country}{prefix}-{id}"

    def wrong_separator():
        country = random.choice(['+32 ', '0'])
        prefix = "4" + str(random.randint(5, 9)) + str(random.randint(0, 9))
        id = " ".join( str(random.randint(0, 99)).rjust(2, '0') for _ in range(4) )
        return f"{country}{prefix} {id}"


    return random.choice([wrong_country, wrong_prefix, wrong_id_size, wrong_separator])()

def random_line():
    return random.choice([random_phone_number, random_crap])()

with open('input.txt', 'w') as out:
    for _ in range(1000):
        print(random_line(), file=out)
