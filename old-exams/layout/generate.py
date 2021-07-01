import random
from faker import Faker
from faker.providers import internet

rnd = random.Random(46412)
Faker.seed(rnd.randint(0, 1000))
fake = Faker()
fake.add_provider(internet)


with open('input.txt', 'w', encoding='utf-8') as file:
    for _ in range(1000):
        name = fake.name()
        ip = fake.ipv4()
        country = fake.country()

        print(f'{name} {ip} {country}', file=file)

