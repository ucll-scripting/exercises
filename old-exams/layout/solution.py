import sys
import re


data = []

for line in sys.stdin:
    match = re.fullmatch(r'(.*) (\d+\.\d+\.\d+\.\d+) (.*)', line.strip())
    name = match.group(1)
    ip = match.group(2)
    country = match.group(3)
    data.append((name, ip, country))

widths = [ max(len(row[i]) for row in data) for i in range(3) ]

for name, ip, country in data:
    name = name.rjust(widths[0])
    ip = ip.ljust(widths[1])
    print(f'{name} {ip} {country}')