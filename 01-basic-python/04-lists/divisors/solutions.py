def divisors(n):
    return [ k for k in range(1, n + 1) if n % k == 0 ]