def count_divisors(n):
    result = 0

    for i in range(1, n):
        if n % i == 0:
            result += 1

    return result