from verilib import *

output_file = 'output.txt'

assert_linecount(output_file, 365)
assert_lines_match_regex(output_file, r'-?\d+')
assert_file_contents_hash_to(output_file, '2e6357dfe5223a11fa2794dfaad8269d4d33041ea5c263b906bed08442637506')
compute_code_for_file(output_file)
