from pandas import read_csv, set_option
from sys import argv, exit


series_name = argv[1]

tb = read_csv('../title-basics.tsv', sep='\t', low_memory=False)
te = read_csv('../title-episodes.tsv', sep='\t', low_memory=False)
tr = read_csv('../title-ratings.tsv', sep='\t', low_memory=False)
series = tb[(tb.primaryTitle == series_name) & (tb.titleType == 'tvSeries')]

if len(series) != 1:
    series = tb[tb.tconst == series_name]

    if len(series) != 1:
        print('Ambiguous query!')
        print(series.to_string(index=False))
        exit(-1)

id = series.iloc[0].tconst
episodes = te[te.parentTconst == id]
episodes_ids = episodes.tconst
joined = episodes.set_index('tconst').join(tr.set_index('tconst'), how='inner').join(tb.set_index('tconst'))
print(joined.sort_values(['averageRating'], ascending=False)[['seasonNumber', 'episodeNumber', 'originalTitle', 'averageRating']].to_string(index=False))