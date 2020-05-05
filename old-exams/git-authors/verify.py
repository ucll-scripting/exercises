from verilib import *

output_file = 'output.txt'

assert_linecount(output_file, 191)
assert_file_contents_hash_to(output_file, 'baf4d61a68bc22f9dca9d948b2f60b283d9595f0b89511315d8d172a1f3c784e')
compute_code_for_file(output_file)
