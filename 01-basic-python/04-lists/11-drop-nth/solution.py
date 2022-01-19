# Using +
def drop_nth(xs, n):
    return xs[:n] + xs[n+1:]

# Using *
def drop_nth(xs, n):
    return [ *xs[:n], *xs[n+1:] ]
