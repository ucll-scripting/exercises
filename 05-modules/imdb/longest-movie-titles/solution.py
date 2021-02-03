from pandas import read_csv, set_option, concat
import csv

set_option('display.max_colwidth', -1)
mylist = []
for chunk in  read_csv('../title-basics.tsv', sep='\t', chunksize=20000):
    mylist.append(chunk)
data = concat(mylist, axis= 0)
del mylist
data = data.loc[data.titleType == 'movie']
data['primaryTitleLength'] = data.primaryTitle.apply(len)
data = data.sort_values(['primaryTitleLength'], ascending=False)
print(data.primaryTitle.head(100).to_string(index=False))
