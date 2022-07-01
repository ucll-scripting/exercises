import sys


words = [word.strip() for word in sys.stdin.readlines()]


for word in words:
    # abcdefgh
    # MMMMWWWW
    if any(letter not in word for letter in 'abcd'):
        continue

    if word[0] == 'a' or word[1] == 'b' or word[2] == 'c' or word[3] == 'd':
        continue

    if any(letter in word for letter in 'efgh'):
        continue

    # xxxxxxxx
    # WWWWCWWW
    indices = [i for i in range(len(word)) if word[i] == 'x']

    if indices != [4]:
        continue

    print(word)