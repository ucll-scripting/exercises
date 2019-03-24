from pandas import read_csv, set_option


set_option('display.max_colwidth', -1)
data = read_csv('../title-basics.tsv', sep='\t', low_memory=False)
data = data.loc[data.titleType == 'movie']
data['primaryTitleLength'] = data.primaryTitle.apply(len)
data = data.sort_values(['primaryTitleLength'], ascending=False)
print(data.primaryTitle.head(100).to_string(index=False))
