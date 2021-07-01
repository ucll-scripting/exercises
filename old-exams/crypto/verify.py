from verilib import *

output_file = 'output.txt'

assert_linecount(output_file, 1000)
assert_lines_match_regex(output_file, r'.* [0-9.]+ [0-9.]+ [0-9.]+')
assert_file_contents_hash_to(output_file, '41dc381218ab4e31afbb14279bdeb275e3fab31738840bf6203b09d176cc42bdd3e9ec1d17d32982a515c41937a055696dfa291ed20375796073ef91e6703d15')
compute_code_for_file(output_file)
