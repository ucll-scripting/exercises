from verilib import *

output_file = 'output.txt'

assert_linecount(output_file, 100)
assert_lines_match_regex(output_file, r'mv (\d+)\.unknown \1.(png|gif|tiff|jpeg|bmp)')
assert_file_contents_hash_to(output_file, '41faa115d9b37986b1a604c37bbe9c85d2b6d83f3b480a340672c72dd0e493b0e38fcaa2b429aa1f47275b091f35ce8e5e902c8743a8ef8530bfd5a5c7f3ae87')
compute_code_for_file(output_file)
