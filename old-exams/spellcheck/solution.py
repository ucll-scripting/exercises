import re


with open('dictionary.txt') as f:
    dictionary = set(f.read().splitlines())

with open('text.txt') as f:
    text = f.read()

words = re.findall(r'\w+', text)

misspelled_words = sorted({word for word in words if word not in dictionary})

print("\n".join(misspelled_words))
