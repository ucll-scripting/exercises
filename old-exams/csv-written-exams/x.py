import csv
with open('exam-schedule.csv') as file:
    reader = csv.DictReader(file)
    list = []
    for row in reader:
        if row['Ex. Soortx'] == 'S':
            lector_id = row['Lector']
            list.append(lector_id)
    d = dict()
    for i in list:
        d[i] = d.get(i,0) + 1
    
    list_more_than_one_lector = []
    list = []
    for i in d.keys():
        lectors = i.split('/')
        if len(lectors) > 1:
            list_more_than_one_lector.append(i)
            list.append(lectors)
 
    for lectors in list: 
        for lector in lectors:
            d[lector] = d.get(lector,0) + 1
            
    for i in list_more_than_one_lector:
        del d[i]
    
    d = dict(sorted(d.items(),key=lambda x : x[0]))
with open('output.txt', 'w') as f:
    for key,value in d.items():
        f.write(f"{key} {value}\n")
        
            
            
        
        
        