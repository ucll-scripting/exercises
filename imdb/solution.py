from tabulate import tabulate
from sys import stderr
import pandas
import csv
import re


def log(string):
    print(string, file=stderr, flush=True)

def read(filename):
    log(f'Reading {filename}...')

    with open(filename, encoding='utf-8') as file:
        return list(csv.DictReader(file, dialect='excel-tab'))

title_basic = read('title-basics.tsv')


def find_top_longest_movies():
    log('Finding longest movies')
    global title_basic
    movie_runtime_pairs = ( (row['primaryTitle'], int(row['runtimeMinutes'])) for row in title_basic if  row['titleType'] == 'movie' and str.isnumeric(row['runtimeMinutes']) )
    sorted_by_runtime = sorted(movie_runtime_pairs, key=lambda pair: pair[1], reverse=True)

    print('Top 100 longest movies')
    print(tabulate(sorted_by_runtime[:100], headers=['Title', 'Runtime']))


def find_top_longest_movie_titles():
    log('Finding longest movie titles')
    global title_basic
    titles = ( row['primaryTitle'] for row in title_basic if row['titleType'] == 'movie' )
    sorted_by_title_length = sorted(titles, key=len, reverse=True)

    print('Top 100 longest titles')
    top = sorted_by_title_length[:100]
    print(tabulate(((title, len(title)) for title in top), headers=['Title', 'Title Length']))


def counts_by_type():
    log('Computing counts by types')
    table = {}
    for row in title_basic:
        type = row['titleType']
        old_count = table.setdefault(type, 0)
        new_count = old_count + 1
        table[type] = new_count
    print('Counts by type')
    print(tabulate( sorted(table.items(), key=lambda x: x[1], reverse=True), headers=['Type', 'Count']))



# for f in [ find_top_longest_movies,
#            find_top_longest_movie_titles,
#            counts_by_type ]:
#     f()
#     print('')
