def target_sum(ns, target):
    for x in ns:
        for y in ns:
            if x + y == target:
                return True
    return False
