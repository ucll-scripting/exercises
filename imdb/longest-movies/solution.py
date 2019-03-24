from pandas import read_csv


title_basics = read_csv('../title-basics.tsv', sep='\t', low_memory=False)
print(title_basics[title_basics.titleType == 'movie'][title_basics.runtimeMinutes != r'\N'].astype( { 'runtimeMinutes': 'int32' } ).sort_values(['runtimeMinutes'], ascending=False).loc[:,['primaryTitle', 'runtimeMinutes']].head(100).to_string(index=False))
