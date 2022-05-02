# Write your code here
import re

def three_to_ten_times_abc(strings):
    return re.fullmatch('(abc){3,10}',strings)