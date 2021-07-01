from verilib import *

output_file = 'output.txt'

assert_linecount(output_file, 16128)
assert_lines_match_regex(output_file, r'[QWERTYUIOP]{6}')
assert_file_contents_hash_to(output_file, '1a6122712a0f3414b0ae7aed2dc6354c2b2cbe26ae86560d47df0d0fc622ddc70ab44e2525f6d0de11ec7bf1f23eef5e10c8603780d63e3a510d5d1fcdf1be02')
compute_code_for_file(output_file)
