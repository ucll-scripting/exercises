# Write your code here
import re
def one_or_more_abc(string):
    return re.fullmatch('(abc)+',string)