from verilib import *

output_file = 'output.txt'

assert_linecount(output_file, 1000)
assert_lines_match_regex(output_file, r'\d+ .*')
assert_file_contents_hash_to(output_file, '665a9f28aff36e4f7014c67b0f61a4fb4e7498b1e7f5c28ec6e4f0f90f51008b6f44ab3309062066758a275d663c1e90b145afd5f84f821ff763da26014acf53')
compute_code_for_file(output_file)
