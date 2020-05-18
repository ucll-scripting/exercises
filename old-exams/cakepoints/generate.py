import hashlib
import random
import datetime



random.seed(463)


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
    return f"{fname} {lname}"

names = list(set(random_name() for _ in range(200)))
names.sort()
random.shuffle(names)

with open('input.txt', 'w') as out:
    for name in names:
        earned = random.randint(0, 10)
        claimed = random.randint(0, earned)
        ops = [ random.choice("+++-") for _ in range(random.randint(1, 20)) ]
        out.write(f'{name}:{claimed}/{earned} {"".join(ops)}\n')
