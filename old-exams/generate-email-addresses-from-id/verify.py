from verilib import *


output_file = 'output.txt'

assert_linecount(output_file, 10000)
assert_lines_match_regex(output_file, r'[rsu]\d{7}@(student\.)?ucll.be')
assert_file_contents_hash_to(output_file, '3d8e1fe1e4653432ccdadc2343c050e0e4837353f72d9f29246f683f9104372d')
compute_code_for_file(output_file)
