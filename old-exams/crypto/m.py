
import json

filename = "input.json"
with open(filename,'r') as f:
    content = json.load(f)
    
list = []
    
for i in content:
    list.append((i["currency"],i["history"]))

with open("output.txt",'w') as f:
    for name,history in list:
        f.write(f"{name} {min(history)} {max(history)} {history[-1]}\n")
        
        