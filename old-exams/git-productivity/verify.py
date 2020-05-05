from verilib import *

output_file = 'output.txt'

assert_linecount(output_file, 49)
assert_lines_match_regex(output_file, r'.*: \d+')
assert_file_contents_hash_to(output_file, '2cf16250a63b05864249ef3a01337b9136a378d9b311b9401591eb0316e7d229')
compute_code_for_file(output_file)
