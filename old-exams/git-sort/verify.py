from verilib import *

output_file = 'output.txt'

assert_linecount(output_file, 5999)
assert_file_contents_hash_to(output_file, 'dfe98f9d80f44b2b328bdfa293c0c171b03d7f6b8210802f0661b41a18e587fa')
compute_code_for_file(output_file)
