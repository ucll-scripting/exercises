from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import regex_test
from scripting.assertions import assert_truthy, assert_falsey


with regex_test('contains_a') as (match, no_match):
    match('a')
    match('ab')
    match('aaaa')
    match('xax')
    match('xxaa')

    no_match('')
    no_match('b')
