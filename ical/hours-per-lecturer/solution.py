from datetime import timedelta
import ics
import sys
import re


# utf-8 necessary to deal with accented names correctly
with open(sys.argv[1], encoding='utf-8') as file:
    calendar = ics.Calendar(file.read())

table = {}

for event in calendar.events:
    match = re.search(r'Lector\(en\):(.*)\Z', event.description, re.DOTALL)
    if not match:
        print(f"Error while parsing\n{event.description}")
        sys.exit(-1)
    else:
        for name in re.split("\n", match.group(1).strip()):
            # Skip events with no lecturers
            if name:
                table[name] = table.get(name, timedelta(0)) + event.duration


for name, duration in sorted(table.items(), key=lambda pair: -pair[1]):
    print(f"{name}: {duration.total_seconds() / 3600}")
