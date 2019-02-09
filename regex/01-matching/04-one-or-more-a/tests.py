from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import regex_test
from scripting.assertions import assert_truthy, assert_falsey


with regex_test('one_or_more_a') as (match, no_match):
    match('a')
    match('aa')
    match('aaa')
    match('aaaa')
    match('aaaaa')

    no_match('')
    no_match('b')
    no_match('ab')
    no_match('aab')
    no_match('ba')
