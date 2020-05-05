from verilib import *

output_file = 'output.txt'

assert_linecount(output_file, 10000)
assert_file_contents_hash_to(output_file, '18b580bbcc9195b624d860973c259b04a15aeac08676fc2335c1542946fee7a2')
compute_code_for_file(output_file)
