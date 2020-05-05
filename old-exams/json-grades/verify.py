from verilib import *

output_file = 'output.txt'

assert_linecount(output_file, 100)
assert_lines_match_regex(output_file, r'r\d{7} \d{1,2}')
assert_file_contents_hash_to(output_file, 'dbe90972b9a4eba2478c49c3f1a85da2dad9029aa316cd7fc3b67c1e75d4d384')
compute_code_for_file(output_file)
