from sys import argv, exit
import csv


def second(xs):
    return xs[1]


table = {}

with open("C:\\Users\\Ninov\\Downloads\\title.episode.tsv\\data.tsv", encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter='\t', quoting=csv.QUOTE_NONE)
    for row in reader:
        id = row['parentTconst']
        if id not in table:
            table[id] = 0
        table[id] += 1


max_episode_count = max(table.values())
print(f'Max episode count: {max_episode_count}')
series = { series_id for series_id, episode_count in table.items() if episode_count == max_episode_count }

with open("C:\\Users\\Ninov\\Downloads\\title.basics.tsv\\data.tsv", encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter='\t', quoting=csv.QUOTE_NONE)
    for row in reader:
        if row['tconst'] in series:
            print(row['primaryTitle'])
