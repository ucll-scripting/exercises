with open('input.txt') as f:
    with open('output.txt', 'w') as out:
        for line in f:
            name, data = line.strip().split(':')
            frac, ops = data.split(' ')
            cashed, earned = map(int, frac.split('/'))

            earned += ops.count('+')
            cashed += ops.count('-')

            out.write(f"{name}:{cashed}/{earned}\n")
