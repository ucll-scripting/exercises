from verilib import *

output_file = 'output.txt'

check_for_existing_solution_key()
assert_linecount(output_file, 12)
assert_lines_match_regex(output_file, r'\s+[A-Z][a-z]+ \**')
assert_file_contents_hash_to(output_file, '1d389a709a1f5fd58d462e82a364fc9a499a77f61ac60b61745ead76972637ae6dae31d3a249cfee388b193fb76467e6085d8ee090653e165479f444db033c0c')
compute_code_for_file(output_file)
