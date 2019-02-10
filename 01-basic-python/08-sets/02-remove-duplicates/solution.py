def remove_duplicates(xs):
    found = set()
    result = []
    for x in xs:
        if x not in found:
            result.append(x)
            found.add(x)
    return result


def remove_duplicates_using_list(xs):
    found = []
    result = []
    for x in xs:
        if x not in found:
            result.append(x)
            found.append(x)
    return result
