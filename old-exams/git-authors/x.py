
with open('input.txt') as input:
    with open('output.txt','w') as output:
        s = set()
        for line in input:
            if line.startswith('Author'):
                name = line.strip().split(' ')[1:-1]
                s.add(" ".join(name))
        s = sorted(s)
        for i in s:
            output.write(f'{i}\n') 