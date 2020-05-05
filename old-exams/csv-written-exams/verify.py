from verilib import *

output_file = 'output.txt'

assert_linecount(output_file, 149)
assert_lines_match_regex(output_file, r'U\d{7} \d+')
assert_file_contents_hash_to(output_file, '2d66d8081832a82e787f4981dde1c17d26754580fa54f57f73db678f11b89524')
compute_code_for_file(output_file)
