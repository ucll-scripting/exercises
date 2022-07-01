import random
import string

rnd = random.Random(45141)


DICTIONARY_SIZE = 200000
ERROR_RATE = 0.01
NPARAGRAPHS = 10000


def random_word():
    return ''.join(rnd.choices(string.ascii_lowercase, k=rnd.randint(2, 16)))


dictionary = sorted({random_word() for _ in range(DICTIONARY_SIZE)})


def random_dictionary_word():
    return random.choice(dictionary)


def generate_words(count):
    def randword():
        return random_dictionary_word() if rnd.random() > ERROR_RATE else random_word()
    return [ randword() for _ in range(count)]


def generate_sentence():
    def generate_subsentence():
        return ' '.join(generate_words(rnd.randint(5, 20)))
    return ", ".join(generate_subsentence() for _ in range(rnd.randint(1, 5))) + "."


def generate_paragraph():
    return ' '.join(generate_sentence() for _ in range(rnd.randint(1, 5)))


def generate_text():
    return '\n\n'.join(generate_paragraph() for _ in range(NPARAGRAPHS))


with open('dictionary.txt', 'w') as f:
    f.write('\n'.join(dictionary))

with open('text.txt', 'w') as f:
    f.write(generate_text())
