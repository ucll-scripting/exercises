# Write your code here
import imp


import re
def hide_email_addresses(string):
    def replace(match):
        return '*'*len(match.group(0))
    return re.sub(r'\w+@[.\w]+',replace, string)