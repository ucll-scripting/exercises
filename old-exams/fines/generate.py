import random
import csv
import re
from faker import Faker
from faker.providers import automotive
from faker.providers import address

NVIOLATIONS = 1048576 + 100

rnd = random.Random(34460)
Faker.seed(510348)
fake = Faker()


addresses = [fake.address() for _ in range(10000)]
plates = [fake.license_plate() for _ in range(100000)]


print('This might take some time...')

violations = []
while len(violations) < NVIOLATIONS:
    n = rnd.randint(10, 1000)
    license_plate = rnd.choice(plates)
    if not re.fullmatch(r'[a-zA-Z0-9 -]+', license_plate):
        continue
    for _ in range(n):
        date = fake.date_time_this_century()
        address = rnd.choice(addresses)
        violation = {
            "date": date,
            "license_plate": license_plate,
            "speed": rnd.randint(120, 250),
            "address": address,
        }
        violations.append(violation)

rnd.shuffle(violations)

with open('violations.csv', 'w', newline='') as file:
    field_names = ['date', 'license_plate', 'speed', 'address']
    writer = csv.DictWriter(file, field_names)
    writer.writeheader()

    for violation in violations:
        writer.writerow(violation)
