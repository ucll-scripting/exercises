def median(ns):
    sorted_ns = sorted(ns)
    i = len(sorted_ns) // 2

    if len(sorted_ns) % 2 == 0:
        return (sorted_ns[i - 1] + sorted_ns[i]) / 2
    else:
        return sorted_ns[i]