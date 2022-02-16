from verilib import *

output_file = 'output.txt'

assert_linecount(output_file, 346)
assert_lines_match_regex(output_file, r'\*+ <<[a-zA-Z0-9]+,.*>>')
assert_file_contents_hash_to(output_file, '01ec7b0945022ee46b9ee5505103a429c60d66edb114d1b8ce07dbb9e6f4382ec40cda3121ce0dd8818803c5381693a76d52cc0bd2219f64bd78d97dccb74a74')
compute_code_for_file(output_file)
