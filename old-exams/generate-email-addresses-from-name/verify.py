from verilib import *

output_file = 'output.txt'

assert_linecount(output_file, 500)
assert_lines_match_regex(output_file, r'[a-z.]+@student.ucll.be')
assert_file_contents_hash_to(output_file, 'ac479646f76c5f67b63993db344e8632a7155c33d99a2930bc1589fecb6b5a7c')
compute_code_for_file(output_file)
