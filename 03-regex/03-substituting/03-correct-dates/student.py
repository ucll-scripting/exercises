# Write your code here
import re
def correct_dates(string):
    return re.sub(r'([1-9]|1[1-2])/([1-9]|[1-3][0-1])/([0-9]+)',r'\2/\1/\3',string)
    