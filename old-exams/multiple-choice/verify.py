from verilib import *

output_file = 'output.txt'

assert_linecount(output_file, 964)
assert_lines_match_regex(output_file, r'[A-Za-z -]+ \d+')
assert_file_contents_hash_to(output_file, '8c148d46d985bb1a4b386f6ccacbe65471066b6f4bf7de2cd7b4a960a75e8c91')
compute_code_for_file(output_file)
