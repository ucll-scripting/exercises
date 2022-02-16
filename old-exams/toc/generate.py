import random
from faker import Faker


rnd = random.Random(7947)
Faker.seed(rnd.randint(0, 1000))
fake = Faker()



def paragraph(file):
    for _ in range(rnd.randint(1, 5)):
        print(fake.paragraph(), file=file)
    print('', file=file)


header_level = 1
id_counter = 1
def header(file):
    global header_level, id_counter
    title = fake.sentence()
    id = f'sec{id_counter}'
    id_counter += 1
    print(f"[#{id}]", file=file)
    print("=" * header_level + " " + title, file=file)
    print("", file=file)
    header_level = max(1, header_level + rnd.choice([-4, -3, -2, -1, 0, 0, 0, 0, 1, 1, 1, 1, 1]))


def bullet_points(file):
    level = 0
    for _ in range(rnd.randint(3, 15)):
        text = fake.sentence()
        bullets = "*" * level
        print(f'{bullets} {text}', file=file)
        level = max(0, level + rnd.choice([-3,-2,-1,0,0,0,0,0,1,1,1,1]))
    print('', file=file)


with open('input.asciidoc', 'w') as file:
    header(file)
    for _ in range(1000):
        rnd.choice([paragraph, header, bullet_points])(file)
