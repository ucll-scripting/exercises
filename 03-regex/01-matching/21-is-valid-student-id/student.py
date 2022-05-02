# Write your code here
import re
def is_valid_student_id(string):
    return re.fullmatch('[sSrR][0-9]{7}',string)