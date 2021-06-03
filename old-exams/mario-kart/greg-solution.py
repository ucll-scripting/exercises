# Because Greg does not like loops

from itertools import groupby


def first(xs):
    return xs[0]

def second(xs):
    return xs[1]

with open('input.txt') as file:
    print("\n".join([ first(x) for x in sorted((x, sum(map(first, y))) for x, y in groupby(sorted(enumerate(line.strip() for line in file), key=second), key=second), key=second) ][:10]))