with open('attending.txt') as f:
    attending = set( line.strip().lower() for line in f )

with open('all.txt') as f:
    with open('absentees.txt', 'w') as out:
        for line in f:
            line = line.strip().lower()
            if line not in attending:
                out.write(f'{line}\n')
