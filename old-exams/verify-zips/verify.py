from verilib import *

output_file = 'output.txt'

assert_linecount(output_file, 50)
assert_lines_match_regex(output_file, r'sub\d{3}.zip')
assert_file_contents_hash_to(output_file, '024567b41814c02e4de74771af4dd329c184031a6d3edb4a3d8586ff3e4ca1be32b0b6f14c1c6d03d8b823e0c56f67d4310e513ebdbb73f56fa644f12d5364c9')
compute_code_for_file(output_file)
