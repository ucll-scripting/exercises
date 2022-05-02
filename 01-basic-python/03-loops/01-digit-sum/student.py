def digit_sum(n):
    result = 0
    while n > 0:
        result += n % 10
        n = n // 10
    return result