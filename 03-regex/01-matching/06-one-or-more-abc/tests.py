from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import regex_test
from scripting.assertions import assert_truthy, assert_falsey


with regex_test('one_or_more_abc') as (match, no_match):
    match('abc')
    match('abcabc')
    match('abcabcabc')
    match('abcabcabcabc')

    no_match('')
    no_match('a')
    no_match('ab')
    no_match('abcabcab')
    no_match('bcabca')
