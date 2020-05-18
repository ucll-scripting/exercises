from verilib import *


output_file = 'output.txt'

assert_linecount(output_file, 510)
assert_file_contents_hash_to(output_file, '004f58b7b161c200c1d525fd73269fda29f41ee6dd2816ea6b8601a153ee7357')
compute_code_for_file(output_file)
