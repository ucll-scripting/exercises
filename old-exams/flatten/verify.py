from verilib import *


output_file = 'output.txt'

assert_linecount(output_file, 10592)
assert_lines_match_regex(output_file, r'[rs]\d{7}')
assert_file_contents_hash_to(output_file, 'a55fd58510855901d4a366181b21a4940e189050cd644077ed747d1aa98b060c')
compute_code_for_file(output_file)
