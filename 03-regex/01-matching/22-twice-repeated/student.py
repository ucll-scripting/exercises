# Write your code here
import re
def twice_repeated(string):
    return re.fullmatch(r'(.)\1',string)