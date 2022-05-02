# Write your code here
import re
def parse_time(string):
    match = re.fullmatch(r'(\d{2}):(\d{2}):(\d{2})(?:\.(\d{3}))?', string)
    
    if match:
        return tuple([int(x) for x in match.groups('000')])
    else:
        return None
  

