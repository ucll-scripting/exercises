from verilib import *

output_file = 'output.txt'

check_for_existing_solution_key()
assert_linecount(output_file, 6)
assert_lines_match_regex(output_file, r'[a-z]{8}')
assert_lines_sorted_by(output_file, lambda x: x)
assert_file_contents_hash_to(output_file, '1bbd3893afc38f90f823f141555f5f68984c8812bc7e21c04acdfa309fbd169ac8762c7ce65c5f17f67760fbbaf0a900694dd928a9ad87fef8a70c49f60cb09c')
compute_code_for_file(output_file)
