import datetime
import random
import json
import math

rnd = random.Random(46412)


def random_temperatures(month):
    avg = round(math.sin(2 * math.pi * (month - 4) / 11) * 20 + 10)

    return [ round(rnd.gauss(avg, 5)) for _ in range(24) ]


current = datetime.datetime(year=2019,month=1,day=1)
dates = []

while current.year == 2019:
    dates.append(current)
    current += datetime.timedelta(days=1)

rnd.shuffle(dates)

data = { date.strftime('%d/%m/%Y'): random_temperatures(date.month) for date in dates }

with open('input.txt', 'w') as file:
    print(json.dumps(data), file=file)
