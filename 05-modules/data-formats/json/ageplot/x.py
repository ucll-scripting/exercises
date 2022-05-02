import json
import sys
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

with open(sys.argv[1], "r") as file:
    a = json.loads(file.read())
    
# AGEGROUP COUNT
# for i in a
# i[AGEGROUP] and i[COUNT]
# o = [(AGEGROUP,COUNT),...]
# for a,c in o:
# if a in result:    result = {AGEGROUP:COUNT}
# result[a] += c
# else: result[a] = c

o = [(i["AGEGROUP"],i["COUNT"]) for i in a]
result = {}
for a,c in o:
    if a in result:
        result[a] += c
    else:
        result[a] = c
        
age_groups = sorted(result.keys())
counts = [ result[age_group] for age_group in age_groups ]
        
plt.rcdefaults()
fig, ax = plt.subplots()
ax.barh(range(len(age_groups)), counts)
ax.set_yticklabels([0, *age_groups])
plt.show()