def median(ns):
    ns = sorted(ns)
    i = len(ns) // 2

    if len(ns) % 2 == 0:
        return (ns[i - 1] + ns[i]) / 2
    else:
        return ns[i]