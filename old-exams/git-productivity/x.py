with open('input.txt') as input:
    with open('output.txt','w') as output:
        d = dict()
        for line in input:
            if line.startswith('Author'):
                d[' '.join(line.strip().split(' ')[1:-1])] = d.get(' '.join(line.strip().split(' ')[1:-1]),0) + 1
        for name,count in sorted(d.items(),key=lambda x: x[1],reverse=True):
            output.write(f'{name}: {count}\n')