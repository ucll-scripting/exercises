from cmath import inf
import csv

from numpy import sort
with open("exam-schedule.csv","r") as csv_file:
    # reader = csv.DictReader(csv_file)
    # unique_date_moment_location = set()
    # unique = set()
    # for row in reader:
    #     unique.add((row["Datum"],row["Dagdeel"],row["Lokaal"]))
    # for i in unique:
    #     unique_date_moment_location.add(i)
    # print(unique_date_moment_location)
    
    content = csv_file.readlines()[1:]
    with open("output.txt",'w') as output:
        for index,row in enumerate(content):
            row_split = row.split(',')
            if index == 0:
                output.write(row)
            elif row_split[3] == content[index-1].split(",")[3] and row_split[5] == content[index-1].split(",")[5] and row_split[9] == content[index-1].split(",")[9]:
                output.write(row)
            else:
                output.write("\n"+row)
                
    with open("output.txt", "r") as output:
        rows_together = output.read()
        rows = rows_together.split('\n\n')
        x = []
        for row in rows:
            columns= row.split('\n')
            x.append(tuple((columns[0].split(',')[-1],len(columns))))
        

        d = dict()
        for lokaal,aantal in x:
            d[lokaal] = 0
        for lokaal,aantal in x:
            if aantal > d[lokaal]:
                d[lokaal] = aantal
        sort_by_key = dict(sorted(d.items(),key=lambda item:item[0]))

        
     
   
    with open("output.txt",'w') as _:
        for key,value in sort_by_key.items():
            _.write(f"{key} {value}\n")