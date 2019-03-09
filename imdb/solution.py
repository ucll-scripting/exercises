from contextlib import contextmanager
import csv



@contextmanager
def open_tsv(filename):
    with open(filename, encoding='utf-8') as file:
        yield csv.DictReader(file, dialect='excel-tab')


def find_longest():
    with open_tsv('title-basics.tsv') as tsv:
        return max(int(row['runtimeMinutes']) for row in tsv if str.isnumeric(row['runtimeMinutes']))


def count_type(type):
    with open_tsv('title-basics.tsv') as tsv:
        return sum(1 for row in tsv if row['titleType'] == type)


def find_people_with_name(name):
    with open_tsv('name-basics.tsv') as tsv:
        return [ row for row in tsv if row['primaryName'] == name ]


sergio = find_people_with_name('Sergio Leone')[0]
