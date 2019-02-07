def frequencies(xs):
    result = {}

    for x in xs:
        if x not in result:
            result[x] = 0

        result[x] += 1

    return result