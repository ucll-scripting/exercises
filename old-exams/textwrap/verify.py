from verilib import *

output_file = 'output.txt'

assert_linecount(output_file, 20053)
assert_file_contents_hash_to(output_file, 'fc2319723ce2790142564efcfd7f205fc3b78193a9aff721905f1c8a8ae83c5d')
compute_code_for_file(output_file)
