def containsDuplicatesNaive(ns):
    for i in range(len(ns)):
        for j in range(i+1, len(ns)):
            if ns[i] == ns[j]:
                return True
    return False

def containsDuplicatesWithSets(ns):
    return len(set(ns)) != len(ns)


from timeit import timeit


def benchmark(n):
    ns = list(range(n))

    def runNaive():
        return containsDuplicatesNaive(ns)

    def runWithSets():
        return containsDuplicatesWithSets(ns)

    print(f"{n} elements")
    t1 = timeit(runNaive, number=10)
    print(f"Naive method: {t1}s")
    t2 = timeit(runWithSets, number=10)
    print(f"Set method  : {t2}s")
    print(f'Speed improvement: {t1/t2}x')
    print('')


benchmark(1000)
benchmark(5000)
benchmark(10000)
benchmark(20000)
