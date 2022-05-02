
with open('input.txt') as f:
    with open('output.txt','w') as g:
        for line in f:
            fname,lname = line.lower().strip().split(' ',maxsplit=1)
            g.write(f"{fname}.{lname.replace(' ','')}@student.ucll.be\n")