import random
import json
from faker import Faker

N = 1000


rnd = random.Random(4231)
Faker.seed(rnd.randint(0, 1000))
fake = Faker()



names = set()
while len(names) < N:
    names.add(fake.name())
names = sorted(names)

scores = set()
while len(scores) < N:
    scores.add(rnd.randint(0, 10000))
scores = sorted(scores)

rnd.shuffle(names)
rnd.shuffle(scores)


data = [{"name": name, "score": score} for name, score in zip(names, scores)]

with open('input.json', 'w') as file:
    json.dump(data, file, indent=4)
