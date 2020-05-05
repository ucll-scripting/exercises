from verilib import *

input_file = 'input.txt'
output_file = 'output.txt'

assert_linecount(output_file, count_lines_in_file(input_file))
assert_lines_match_regex(output_file, r'(.*):(\d+)/(\d+)')
assert_file_contents_hash_to(output_file, 'f577cafb4f7b1ce0412f1b84460870509e9755775db4225e77dc5cc1aa544c8f')
compute_code_for_file(output_file)
