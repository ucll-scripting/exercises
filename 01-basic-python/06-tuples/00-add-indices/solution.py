def add_indices(xs):
    return list(zip(range(len(xs)), xs))

# Better: relying on existing functionality
def add_indices(xs):
    return list(enumerate(xs))
