with open('input.txt') as f:
    with open('output.txt', 'w') as out:
        for line in f:
            print(bin(int(line.strip()))[2:], file=out)