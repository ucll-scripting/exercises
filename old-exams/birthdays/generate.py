import random
import json
from faker import Faker
from faker.providers import person
from datetime import date

NPEOPLE = 1000

rnd = random.Random(45141)
Faker.seed(145834)
fake = Faker()


def random_person():
    name = fake.name()
    birthday = fake.date_between(start_date=date(1980,1,1), end_date=date(2020,1,1))
    return {
        'name': name,
        'birthday': {
            'day': birthday.day,
            'month': birthday.month,
            'year': birthday.year
        }
    }



with open('data.json', 'w') as file:
    data = [random_person() for _ in range(NPEOPLE)]
    json.dump(data, file)