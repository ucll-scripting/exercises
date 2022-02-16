from verilib import *

output_file = 'output.txt'

assert_linecount(output_file, 10001)
assert_lines_match_regex(output_file, r'\d+ [a-zA-Z0-9+/=]{64}')
assert_file_contents_hash_to(output_file, 'c8926d4b841482164f7f2078c52afc6b780e1ad06f95e75efa947b9b582763bb62b627ef1e36461f065145766f2ed6515eaa329f3be5838c4683e25bf9f9ca8e')
compute_code_for_file(output_file)
