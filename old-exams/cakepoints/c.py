import re
import sys
with open('input.txt', 'r') as f:
    content = f.readlines()
    output = []
    for i in content:
        match = re.fullmatch(r'(.*):(\d+)/(\d+) ([+-]*)',i[:-1])
        if match:
            name,exchanged_coins,earned_coins,simple = match.groups()
      
        plus = [x for x in simple if x == '+']
        plus = len(plus)
        min = [x for x in simple if x == '-']
        min = len(min)
    
        output.append(f"{name}:{sum([int(exchanged_coins),int(min)])}/{sum([int(earned_coins),int(plus)])}\n")
        
      

with open('output.txt', 'w') as g:
    for j in output:
        g.write(j)


        
