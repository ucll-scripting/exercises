from verilib import *

output_file = 'absentees.txt'

assert_linecount(output_file, 31414)
assert_lines_match_regex(output_file, r'[rs]\d{7}')
assert_file_contents_hash_to(output_file, 'c0ae3fbf95096aec0e635d5580982789c2922db777681a28abd0f398c0598bb4')
compute_code_for_file(output_file)
