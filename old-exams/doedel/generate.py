import csv
import random
from faker import Faker
from faker.providers import internet

rnd = random.Random(44112)
Faker.seed(rnd.randint(0, 1000))
fake = Faker()

NPEOPLE = 1000


dates = [ f'{str(day).rjust(2, "0")}-06-2021' for day in range(1, 26) ]
vote_counts = list({ rnd.randint(5, NPEOPLE+1) for _ in dates })

assert(len(dates) == len(vote_counts))

def generate_votes(i):
    result = [ 'yes' ] * vote_counts[i] + ['no' ] * (NPEOPLE - vote_counts[i])
    rnd.shuffle(result)
    return result

votes = { dates[i]: generate_votes(i) for i in range(len(dates)) }
names = [ fake.name() for _ in range(NPEOPLE) ]



fieldnames = [ 'name', *dates ]

with open('input.csv', 'w', encoding='utf-8', newline='\n') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(NPEOPLE):
        row = dict((date, votes[date][i]) for date in dates)
        row['name'] = names[i]
        writer.writerow(row)
