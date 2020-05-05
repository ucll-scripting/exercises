import re

with open('input.txt') as f:
    with open('output.txt', 'w') as out:
        for line in f:
            line = re.sub(r'\$HEX\((\d+)\)', lambda m: "0x" + hex(int(m.group(1))).upper()[2:], line)
            out.write(line)