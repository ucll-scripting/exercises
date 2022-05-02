import json

import scipy as sp


with open('input.txt','r') as f:
    contents = json.load(f)
    
    
    x = [(key.split('/'),contents[key]) for key in contents]
    x.sort(key = lambda x: (x[0][2],x[0][1],x[0][0]))
    with open('output.txt','w') as output:
        for i,j in x:
            output.write(str(round(sum(j)/len(j)))+'\n')
    