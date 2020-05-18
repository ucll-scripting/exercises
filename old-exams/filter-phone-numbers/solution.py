import re


with open('input.txt') as f:
    with open('output.txt', 'w') as out:
        for line in f:
            if re.fullmatch(r'(0|\+32-)4[56789]\d-\d{2}-\d{2}-\d{2}', line.strip()):
                out.write(line)