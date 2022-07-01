import hashlib
import random
import sys
import re
import os
from contextlib import contextmanager


SOLUTION_KEY_FILE = 'solution-key.txt'


def debug_mode():
    return 'DIAG' in os.environ


def say(msg, diagnostic=False):
    if debug_mode() or not diagnostic:
        print(msg, file=sys.stderr)


def quit():
    sys.exit(-1)


@contextmanager
def smart_open(filename):
    with open(filename, 'rb') as file:
        first_bytes = file.read(2)

    if first_bytes == b'\xff\xfe' or first_bytes == b'\xfe\xff':
        say('Opening file using UTF16 encoding')
        with open(filename, encoding='utf16') as file:
            yield file
    else:
        say('Opening file using UTF8 encoding')
        with open(filename, encoding='utf-8') as file:
            yield file


def slowhash(answer):
    answer = answer.encode('utf-8')

    for _ in range(10):
        answer = hashlib.sha3_512(answer).digest()

    return answer.hex()


def quickhash(answer):
    return hashlib.sha256(answer.encode('utf-8')).hexdigest()


def count_lines_in_file(filename):
    linecount = 0
    with smart_open(filename) as f:
        for line in f:
            linecount += 1
    return linecount


def assert_linecount(filename, expected):
    say(f'Checking that {filename} does contain {expected} lines...')
    linecount = count_lines_in_file(filename)

    if linecount != expected:
        say(f'{filename} is expected to have {expected} lines, but instead has {linecount}')
        say('If you think the linecount reported here is incorrect, contact a lecturer')
        say("Make sure you don't rely on redirection (e.g. py solution.py > output.txt) when using PowerShell!")
        sys.exit(-1)
    else:
        say(f'SUCCESS: Line count is ok!')


def assert_lines_match_regex(filename, regex):
    say(f'Checking that lines in {filename} are formatted correctly...')

    with smart_open(filename) as f:
        line_index = 0
        for line in f:
            line_index += 1
            if not re.fullmatch(regex, line.rstrip()):
                say(f'Line {line_index} is invalid; its contents are:\n{line}')
                sys.exit(-1)

    say(f'SUCCESS: All lines are formatted correctly!')


def assert_file_contents_matches(filename, regex):
    say(f'Checking if contents match {regex}')

    with smart_open(filename) as f:
        contents = f.read()

    if not re.fullmatch(regex, contents, re.DOTALL | re.MULTILINE):
        say(f'Contents failed to match {regex}')
        sys.exit(-1)

    say(f'SUCCESS: Contents matched {regex}!')


def assert_file_contents_hash_to(filename, expected):
    say(f'Thoroughly checking contents of {filename}...')

    with smart_open(filename) as file:
        contents = "".join([ line.strip() for line in file ])
    actual = slowhash(contents)

    if actual != expected:
        say(f'Expected to get {expected}', diagnostic=True)
        say(f'Got {actual} instead', diagnostic=True)
        say(f"I'm afraid your {filename} does not contain the correct data...")
        say(f"The contents need to be correct to the byte, we're being very strict")
        say(f"Possible mistakes:")
        say(f"* Does the file contain the data in the right format, as specified by the assignment?")
        say(f"* Some assignments require the data to be sorted")
        quit()
    else:
        say(f'SUCCESS: {filename} has correct contents!')


def assert_lines_sorted_by(filename, key_function):
    say('Checking line order...')

    last = None
    lineno = 0

    with smart_open(filename) as f:
        for line in f:
            lineno += 1
            k = key_function(line)
            if lineno != 1 and not k > last:
                say(f"Line #{lineno} is out of place; check the ordering of lines")
                sys.exit(-1)
            last = k

    say('SUCCESS: Line order is ok!')


def generate_salt():
    ndigits = 6
    return hex(random.randint(0, 16**ndigits))[2:].rjust(ndigits, '0')


def generate_code(contents):
    h = quickhash(contents)[:20]
    s = generate_salt()
    return h + s


def check_for_existing_solution_key():
    if os.path.exists(SOLUTION_KEY_FILE):
        say('You already have generated the solution key for this question')
        say(f'You can find it in {SOLUTION_KEY_FILE}')
        say("But since we're so friendly, here is the solution key again:")

        with open(SOLUTION_KEY_FILE, 'r') as f:
            print(f.read().strip())
        quit()


def compute_code_for_file(filename):
    contents = ''

    with smart_open(filename) as f:
        for line in f:
            contents += line.strip()

    say('Your solution is CORRECT!')
    say('Computing solution key...')
    code = generate_code(contents)
    say(f'The solution key for this exercise is:')
    print(code)
    say(f'For your convenience, I have written it to {SOLUTION_KEY_FILE}')
    say(f"This way you don't have to store it yourself")
    with open(SOLUTION_KEY_FILE, 'w') as f:
        f.write(code)
