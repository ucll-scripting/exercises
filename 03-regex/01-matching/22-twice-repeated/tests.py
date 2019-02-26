from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import regex_test
from scripting.assertions import assert_truthy, assert_falsey


with regex_test('twice_repeated') as (match, no_match):
    match('aa')
    match('xx')
    match('11')
    match('..')

    no_match('')
    no_match('a')
    no_match('aaa')
    no_match('aab')
    no_match('aaax')
    no_match('xaaa')
