# Write your code here
import re
def collect_links(string):
    match = re.findall(r'<a href="(.*)">.*</a>',string)
    if match:
        return match
    else:
        return None
    
 

