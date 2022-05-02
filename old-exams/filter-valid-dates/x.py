import datetime
import re

def check_date(day,month,year):
        '''test to see whether the date falls within the scope of a legitimate date'''
        try:
            datetime.datetime(year, month, day)
            return 1
        except ValueError:
            return 0
with open('input.txt') as f:
    with open('output.txt', 'w') as o:
        content = f.readlines()
        for line in content:
            match = re.fullmatch(r'(\d+)-(\d+)-(\d+)',line.strip())
            if match:
                day, month, year = match.groups()
                if check_date(int(day), int(month), int(year)):
                    o.write(line)