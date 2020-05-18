from verilib import *

output_file = 'output.txt'

assert_linecount(output_file, 14)
assert_lines_match_regex(output_file, r'.* \d+')
assert_file_contents_hash_to(output_file, '8347f48c75f6fce71dad0626783a8f027c660644a6020a0c9eb45342fb7f6b3e')
compute_code_for_file(output_file)
