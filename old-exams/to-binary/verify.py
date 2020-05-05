from verilib import *

output_file = 'output.txt'

assert_linecount(output_file, 1000)
assert_lines_match_regex(output_file, r'[01]+')
assert_file_contents_hash_to(output_file, '4ce415cc729a590fe58776e0b6365a79d01937e4981f0003ad1a5d9c490648a4')
compute_code_for_file(output_file)
