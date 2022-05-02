from operator import not_
import re


with open('all.txt','r') as f:
    contents_all = [i.lower() for i in f.readlines()]
with open('attending.txt','r') as g:
    contents_attending = [i.lower() for i in g.readlines()]
    
    
not_attending = [i for i in contents_all if i not in contents_attending]

with open('absentees.txt','w') as h:
    for i in not_attending:
        h.write(i)