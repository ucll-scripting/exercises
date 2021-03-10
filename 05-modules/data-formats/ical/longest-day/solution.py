from datetime import timedelta
import ics
import sys
import re


with open(sys.argv[1], encoding='utf-8') as file:
    calendar = ics.Calendar(file.read())

table = {}

for event in calendar.events:
    date = event.begin.date()
    start = event.begin
    end = event.end

    if date not in table:
        table[date] = (start, end)
    else:
        old_start, old_end = table[date]
        new_start = min(old_start, start)
        new_end = max(old_end, end)
        table[date] = (new_start, new_end)

for date, pair in sorted(table.items(), key=lambda pair: pair[1][1] - pair[1][0], reverse=True):
    start, end = pair
    print(f"{date} {start.time()} {end.time()} {end - start}")

