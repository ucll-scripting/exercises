with open('input.txt') as f:
    with open('output.txt', 'w') as out:
        for line in f:
            name = line.strip()
            parts = name.split(' ')
            fname = parts[0].lower()
            lname = ''.join(parts[1:]).lower()
            print(f'{fname}.{lname}@student.ucll.be', file=out)