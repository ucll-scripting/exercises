from verilib import *

output_file = 'output.txt'

assert_linecount(output_file, 10)
assert_file_contents_hash_to(output_file, '6fdd53f4890ef5a07f24c9a3a2777a2874214d567e96496746efbf788269cdc7')
compute_code_for_file(output_file)
