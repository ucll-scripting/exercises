import hashlib
import random
import datetime

random.seed(450623)

lnames = [
    'Artois',
    'Ausloos',
    'Ausloos',
    'Bekaert',
    'Bogers',
    'Coremans',
    'De Bel',
    'De Clercq',
    'De Smet',
    'De Wyngaert',
    'Dekleermaeker',
    'Geurts',
    'Gevaert',
    'Hamelryck',
    'Happaerts',
    'Hotters',
    'Jacobs',
    'Kaja',
    'Kazantsev',
    'Langui',
    'Leysen',
    'Loddewijkx',
    'Massie',
    'Pasteels',
    'Saint',
    'Sateur',
    'Segal Stanciu',
    'Stalpaert',
    'Swennen',
    'Tashfeen',
    'Tollet',
    'Tyberghein',
    'Van Beersel',
    'Van Beneden',
    'Van den Bosch',
    'Van den Briel',
    'Van der Perre',
    'Van Hecke',
    'Van Kerkhoven',
    'Van Reeth',
    'Van Woensel',
    'Vanbriel',
    'Vandebroeck',
    'Vandenberghen',
    'Vander Hulst',
    'Vanophalvens',
    'Vanspauwen',
    'Verbaendert',
    'Verbeken',
    'Verheyden',
    'Verstraeten',
    'Willendyck',
    'Yermolovich',
    'Zegers',
    'Aerts',
    'Batista Barias',
    'Heylen',
    'Pauwels',
    'Van Esbroeck',
    'Verheyden',
]

fnames = [
    'Arne',
    'Frederik',
    'Lowie',
    'Eline',
    'Darius',
    'Sam',
    'Ruben',
    'Tibo',
    'Karel',
    'Nick',
    'Tim',
    'Tom',
    'Nathan',
    'Axel',
    'Tommi',
    'Kenzo',
    'Sibren',
    'Blenda',
    'Nikita',
    'Kim',
    'Andreas',
    'Gust',
    'Jens',
    'Koen',
    'Filip',
    'Maxime',
    'Andrei',
    'Connor',
    'Wout',
    'Asif',
    'Niels',
    'Ruben',
    'Hendrik',
    'Maarten',
    'Vincent',
    'Abel',
    'Tim',
    'Vito',
    'Wout',
    'Arno',
    'TijsEmiel',
    'Bram',
    'Timothy',
    'Jasper',
    'Jentse',
    'Wouter',
    'Arnaud',
    'Liwady',
    'Sander',
    'Jeroen',
    'Lars',
    'Andrej',
    'Jonas',
    'Bjorn',
    'Franchesca Abigail',
    'Bert',
    'Hans',
    'Jordy',
    'Redginald',
]

def random_name():
    global fnames, lnames
    fname = random.choice(fnames)
    lname = random.choice(lnames)
    return (fname, lname)


authors = list(set( random_name() for _ in range(50) ))
authors.sort()

def random_author():
    global authors
    return random.choice(authors)

def email_address_of(person):
    fname, lname = person
    fname = fname.replace(' ','')
    lname = lname.replace(' ','')
    return f'{fname.lower()}.{lname.lower()}@student.ucll.be'

def random_timestamp():
    day = random.randint(1, 28)
    month = random.randint(1, 12)
    year = random.randint(2010, 2018)
    hour = random.randint(0, 23)
    minute = random.randint(0, 59)
    second = random.randint(0, 59)
    return datetime.datetime(year, month, day, hour, minute, second)

class Commit:
    def __init__(self, hash, author, time, message):
        self.hash = hash
        self.author = author
        self.email = email_address_of(author)
        self.time = time
        self.message = message

    def __str__(self):
        return f'''
commit {self.hash}
Author: {self.author[0]} {self.author[1]} <{self.email}>
Date:   {self.time}

    {self.message}
    '''.strip()

def random_commit(author=None, time=None, message=None):
    hash = hashlib.sha1(str(random.randint(0, 10**9)).encode('utf-8')).hexdigest()
    author = author or random_author()
    time = time or random_timestamp()
    message = message or f'Closed #{random.randint(1, 10000)}'
    return Commit(hash, author, time, message)

def random_commits(n, **kwargs):
    return sorted([ random_commit(**kwargs) for _ in range(n) ], key=lambda x: x.time)


commits = []
freqs = list(range(10, 10+20*len(authors)))
random.shuffle(freqs)

for author in authors:
    n = freqs.pop(0)
    commits.extend(random_commits(n, author=author))

commits.sort(key=lambda x: x.time)

with open('input.txt', 'w') as out:
    out.write("\n\n".join(map(str, commits)))