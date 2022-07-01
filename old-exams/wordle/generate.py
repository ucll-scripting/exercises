import random
import string

rnd = random.Random(45141)

WORD_SIZE = 8
WORD_COUNT = 100000

def random_word():
    return "".join(rnd.choices(string.ascii_lowercase, k=WORD_SIZE))


with open('words.txt', 'w') as file:
    words = { random_word() for _ in range(WORD_COUNT) }
    file.write("\n".join(sorted(words)))
