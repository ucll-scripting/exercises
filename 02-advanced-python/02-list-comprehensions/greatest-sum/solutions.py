def greatest_sum(ns):
    return max([0] + [sum(ns[i:j]) for i in range(0, len(ns)) for j in range(i+1, len(ns))])