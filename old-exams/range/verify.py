from verilib import *

output_file = 'output.txt'

assert_linecount(output_file, 10**6)
assert_lines_match_regex(output_file, r'\d+')
assert_file_contents_hash_to(output_file, 'bf5d8ff22a939829af769c1e1194707cfd67658a140afc6497aa3ecbb1a6180d')
compute_code_for_file(output_file)
