with open('input.txt') as f:
    with open('output.txt', 'w') as out:
        for line in f:
            id = line.strip().lower()
            if id.startswith('u'):
                domain = 'ucll.be'
            else:
                domain = 'student.ucll.be'
            print(f'{id}@{domain}', file=out)