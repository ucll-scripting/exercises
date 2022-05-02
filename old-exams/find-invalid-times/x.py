import re
import datetime


def valid_time(string):
    timeformat = "%H:%M:%S"
    try:
        validtime = datetime.datetime.strptime(string, timeformat)
        return True
    except ValueError:
        return False
    
with open('input.txt', 'r') as f:
    with open('output.txt', 'w') as j:
        content = f.readlines()
        content_with_index = enumerate(content,start=1)
        for index,time in content_with_index:
            match = re.findall(r'\d\d:\d\d:\d\d',time)
            
            for i in match:
                if not valid_time(i):
                    j.write(f"{index} {i}\n")
                
            
    
    
    

