import re
import datetime

def returnDate(string):
    date = re.search(r'Date: (.*)',string)
    date = date.group(1)
    date = datetime.datetime.strptime(date.strip(),"%Y-%m-%d %H:%M:%S")
    return date

with open('input.txt') as input:
    with open('output.txt','w') as output:
        content = input.read()
        match = re.findall(r'commit .*?Closed \#\d+',content,re.DOTALL)
        match.sort(key=returnDate,reverse=True)
        s = '\n\n'.join(match)
        output.write(s)
            