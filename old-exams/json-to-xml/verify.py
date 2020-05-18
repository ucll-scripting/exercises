from verilib import *
import re

output_file = 'output.txt'

def line_key(line):
    line = line.strip()
    if line == '<students>':
        return 'a'
    elif line == '</students>':
        return 'c'

    m = re.search(r'^<student id="(r\d+)', line)
    if not m:
        say('Unexpected error; contact lecturer')
        sys.exit(-1)
    return f'b{m.groups(1)}'

assert_linecount(output_file, 994)
assert_lines_match_regex(output_file, r'</?students>|<student id="r\d+"><grades>(<grade>\d+</grade>)+</grades></student>')
assert_file_contents_hash_to(output_file, '01ac5a138ab1b6dbdc56854246b0f402b93c670e4be00c6255ac37551c912857')
compute_code_for_file(output_file)
