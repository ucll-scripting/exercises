import itertools
import re


for cs in itertools.product(sorted("QWERTYUIOP"), repeat=6):
    pw = ''.join(cs)
    if re.search(r'([AEIOU])\1', pw) and re.search(r'([QWRTYP])\1', pw) and len(set(pw)) == 4:
        print(pw)
