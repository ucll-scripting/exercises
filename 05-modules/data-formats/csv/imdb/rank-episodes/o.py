import csv
import sys

def returnfirst(xs):
    return xs[0]


name = sys.argv[1]

table = {}

with open("C:\\Users\\Ninov\\Downloads\\title.basics.tsv\\data.tsv", encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter='\t', quoting=csv.QUOTE_NONE)
    
    episodes = [row['tconst'] for row in reader if row['originalTitle'] == name and row['titleType'] == 'tvSeries']

with open("C:\\Users\\Ninov\\Downloads\\title.episode.tsv\\data.tsv", encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter='\t', quoting=csv.QUOTE_NONE)
    
    episodesfinal = [ (row['tconst'],row['seasonNumber'],row['episodeNumber']) for row in reader if row['parentTconst'] in episodes]


with open("C:\\Users\\Ninov\\Downloads\\title.ratings.tsv\\data.tsv", encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter='\t', quoting=csv.QUOTE_NONE)
    
    ratings = []
    for row in reader:
        for i in episodesfinal:
            if i[0] == row['tconst']:
                ratings.append(row['averageRating'])
                
                
with open("C:\\Users\\Ninov\\Downloads\\title.basics.tsv\\data.tsv", encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter='\t', quoting=csv.QUOTE_NONE)
    
    result = []
    for row in reader:
        for id,season,episode in episodesfinal:
            if id == row['tconst']:
                result.append((row['originalTitle'],season,episode))


final = sorted(zip(result, ratings), key = lambda x: x[1], reverse=True)
for result,rating in final:
    print(f"S{result[1].rjust(2, '0')}E{result[2].rjust(2, '0')}{result[0].ljust(40,' ')} {rating}")
    
                


