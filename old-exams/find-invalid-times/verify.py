from verilib import *

output_file = 'output.txt'

assert_linecount(output_file, 1335)
assert_lines_match_regex(output_file, r'\d+ [0-9:]+')
assert_file_contents_hash_to(output_file, '977b54ed9a1187fd23a18e5452acda0466190d5519d2a4a6c7f4f3dfb8c65357')
compute_code_for_file(output_file)
