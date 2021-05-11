import matplotlib.pyplot as plt
import json


with open('../covid.json') as file:
    data = json.load(file)


table = {}

for entry in data:
    age_group = entry['AGEGROUP']
    count = entry['COUNT']

    table[age_group] = table.get(age_group, 0) + count


age_groups = sorted(table.keys())
counts = [ table[age_group] for age_group in age_groups ]

plt.rcdefaults()
fig, ax = plt.subplots()
ax.barh(range(len(age_groups)), counts)
ax.set_yticklabels([0, *age_groups])
plt.show()
