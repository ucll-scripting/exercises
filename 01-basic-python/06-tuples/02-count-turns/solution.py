def count_turns(xs):
    result = 0

    for (x, y, z) in zip(xs, xs[1:], xs[2:]):
        if x < y > z or x > y < z:
            result += 1

    return result