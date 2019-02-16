def nth_longest_string(n, strings):
    return sorted(strings, key=len)[-n]