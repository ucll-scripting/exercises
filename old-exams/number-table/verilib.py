import hashlib
import sys
import re
import os


def say(msg, diagnostic=False):
    if 'DIAG' in os.environ or not diagnostic:
        print(msg, file=sys.stderr)


def slowhash(answer):
    answer = answer.encode('utf-8')

    for _ in range(10000000):
        answer = hashlib.sha3_512(answer).digest()

    return answer.hex()


def count_lines_in_file(filename):
    linecount = 0
    with open(filename) as f:
        for line in f:
            linecount += 1
    return linecount


def assert_linecount(filename, expected):
    say(f'Checking that {filename} does contain {expected} lines...')
    linecount = count_lines_in_file(filename)

    if linecount != expected:
        say(f'{filename} is expected to have {expected} lines, but instead has {linecount}')
        sys.exit(-1)
    else:
        say(f'SUCCESS: Line count is ok!')


def assert_lines_match_regex(filename, regex):
    say(f'Checking that lines in {filename} are formatted correctly...')

    with open(filename) as f:
        line_index = 0
        for line in f:
            line_index += 1
            if not re.fullmatch(regex, line.rstrip()):
                say(f'Line {line_index} is invalid; its contents are:\n{line}')
                sys.exit(-1)

    say(f'SUCCESS: All lines are formatted correctly!')


def assert_file_contents_matches(filename, regex):
    say(f'Checking if contents match {regex}')

    with open(filename) as f:
        contents = f.read()

    if not re.fullmatch(regex, contents, re.DOTALL | re.MULTILINE):
        say(f'Contents failed to match {regex}')
        sys.exit(-1)

    say(f'SUCCESS: Contents matched {regex}!')


def assert_file_contents_hash_to(filename, expected):
    say(f'Thoroughly checking contents of {filename}...')
    hash = hashlib.sha256()

    with open(filename) as f:
        for line in f:
            hash.update(line.strip().encode('utf-8'))

    actual = hash.hexdigest()
    if actual != expected:
        say(f'Expected to get {expected}', diagnostic=True)
        say(f'Got {actual} instead', diagnostic=True)
        say(f"I'm afraid your {filename} does not contain the correct data...")
        say(f"The contents need to be correct to the byte, we're being very strict")
        say(f"Possible mistakes:")
        say(f"* Does the file contain the data in the right format, as specified by the assignment?")
        say(f"* Some assignments require the data to be sorted")
        sys.exit(-1)
    else:
        say(f'SUCCESS: {filename} has correct contents!')


def assert_lines_sorted_by(filename, key_function):
    say('Checking line order...')

    last = None
    lineno = 0

    with open(filename) as f:
        for line in f:
            lineno += 1
            k = key_function(line)
            if lineno != 1 and not k > last:
                say(f"Line #{lineno} is out of place; check the ordering of lines")
                sys.exit(-1)
            last = k

    say('SUCCESS: Line order is ok!')


def compute_code_for_file(filename):
    contents = ''

    with open(filename) as f:
        for line in f:
            contents += line.strip()

    say('Your solution is CORRECT!')
    say('Computing solution key... this takes around 10 seconds')
    code = slowhash(contents)[:20]
    say(f'The solution key for this exercise is:')
    print(code)
