from sys import argv, exit
import csv


def create_reader(file):
    return csv.DictReader(file, delimiter='\t', quoting=csv.QUOTE_NONE)


series_name = argv[1]


# Find row(s) containing series_name
with open("../title-basics.tsv", encoding='utf-8') as file:
    reader = create_reader(file)
    rows = [ row for row in reader if row['originalTitle'] == series_name and row['titleType'] == 'tvSeries' ]

# Stop if there we found zero or multiple series with the same name
if len(rows) != 1:
    print(f"Found ${len(rows)} matches")
    exit(-1)

row = rows[0]
series_id = row['tconst']


# Dictionary that associates tconst-ids to data of the corresponding episode
episode_data = {}

# Collect episodes associated with series and store their season and episode_number
with open('../title-episodes.tsv', encoding='utf-8') as file:
    reader = create_reader(file)
    for row in reader:
        if row['parentTconst'] == series_id:
            data = { 'season': int(row['seasonNumber']), 'episode number': int(row['episodeNumber']) }
            episode_data[row['tconst']] = data


# Gather ratings
with open('../title-ratings.tsv', encoding='utf-8') as file:
    reader = create_reader(file)
    for row in reader:
        id = row['tconst']
        if id in episode_data:
            episode_data[id]['rating'] = float(row['averageRating'])

# Gather titles
with open("../title-basics.tsv", encoding='utf-8') as file:
    reader = create_reader(file)
    for row in reader:
        id = row['tconst']
        if id in episode_data:
            episode_data[id]['title'] = row['originalTitle']

# Print data
for data in sorted(episode_data.values(), key=lambda data: data['rating'], reverse=True):
    title = data['title'].ljust(40, ' ')
    rating = data['rating']
    season = str(data['season']).rjust(2, '0')
    epnr = str(data['episode number']).rjust(2, '0')
    print(f"S{season}E{epnr} {title} {rating}")