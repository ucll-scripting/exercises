from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import regex_test
from scripting.assertions import assert_truthy, assert_falsey


with regex_test('one_or_more_b') as (match, no_match):
    match('b')
    match('bb')
    match('bbb')
    match('bbbb')
    match('bbbbb')

    no_match('')
    no_match('a')
    no_match('ab')
    no_match('aab')
    no_match('ba')
