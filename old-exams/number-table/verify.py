from verilib import *

output_file = 'output.txt'

assert_linecount(output_file, 10001)
assert_file_contents_hash_to(output_file, '76d9140f53f92e1d8ca4cff63cf3073c85d93b1cecd14fa2a75257beda399d7e')
compute_code_for_file(output_file)
