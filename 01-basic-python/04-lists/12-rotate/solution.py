def rotate(xs, n):
    for _ in range(n):
        x = xs.pop(0)
        xs.append(x)
