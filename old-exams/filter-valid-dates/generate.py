import random


random.seed(858119)

def generate():
    d = random.randint(1, 35)
    m = random.randint(1, 14)
    y = random.randint(1900, 2400)
    sep = random.choice('-------/:\|,')
    return f'{d}{sep}{m}{sep}{y}'


with open('input.txt', 'w') as out:
    dates = [ generate() for _ in range(1000) ]
    dates.append('29-2-2000')
    dates.append('29-2-2001')
    dates.append('29-2-2002')
    dates.append('29-2-2003')
    dates.append('29-2-2004')
    dates.append('29-2-2100')

    random.shuffle(dates)
    for date in dates:
        print(date, file=out)