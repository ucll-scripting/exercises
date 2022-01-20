def containsDuplicatesNaive(ns):
    for i in range(len(ns)):
        for j in range(i+1, len(ns)):
            if ns[i] == ns[j]:
                return True
    return False

def containsDuplicatesWithSets(ns):
    return len(set(ns)) != len(ns)


from timeit import timeit

ns = list(range(10000))

def runNaive():
    return containsDuplicatesNaive(ns)

def runWithSets():
    return containsDuplicatesWithSets(ns)

print(f"Naive method: {timeit(runNaive, number=10)}s")
print(f"Set method: {timeit(runWithSets, number=10)}s")