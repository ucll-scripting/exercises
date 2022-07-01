from verilib import *

output_file = 'output.txt'

check_for_existing_solution_key()
assert_linecount(output_file, 10114)
assert_lines_match_regex(output_file, r'[a-z]+')
assert_lines_sorted_by(output_file, lambda x: x)
assert_file_contents_hash_to(output_file, '3add46d6ebc13d7966eeb00564c9991d7020ae0c781520fea53e0d4b627692a253967a11e45ed0b0b4be961b0919d4f63781af0255a0957161bc961dab4c3eff')
compute_code_for_file(output_file)
