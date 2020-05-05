with open('input.txt') as f:
    with open('output.txt', 'w') as out:
        for line in f:
            for id in line.strip().split(','):
                out.write(f'{id}\n')