from verilib import *


output_file = 'output.txt'

assert_linecount(output_file, 437)
assert_file_contents_hash_to(output_file, '27cc896718ca0396f1d9de2a6324fc0a8a33960e4e21d1ae7d5075ee2bfda8ce')
compute_code_for_file(output_file)
