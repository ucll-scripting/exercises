
with open('input.txt', 'r') as f:
    with open('output.txt', 'w') as g:
        content = f.readlines()
        for i in content:
            ids = i.split(',')
            for i in ids:
                i = i.strip()
                g.write(f"{i}\n")
    
    
