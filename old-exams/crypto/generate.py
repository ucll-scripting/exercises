import json
import random
from faker import Faker
from faker.providers import internet

rnd = random.Random(1122)
Faker.seed(rnd.randint(0, 1000))
fake = Faker()


NCURRENCIES = 1000


def random_currency():
    currency = fake.cryptocurrency()
    history = [ rnd.randint(1, 10000) / 100 for _ in range(rnd.randint(10, 1000)) ]
    return (currency[1], history)


data = [ { 'currency': currency, 'history': history } for currency, history in (random_currency() for _ in range(NCURRENCIES)) ]

with open('input.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=4)
