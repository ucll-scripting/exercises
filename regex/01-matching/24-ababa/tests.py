from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import regex_test
from scripting.assertions import assert_truthy, assert_falsey


with regex_test('ababa') as (match, no_match):
    match('ababa')
    match('xyxyx')
    match('12121')
    match('aabbaabbaa')
    match('111222111222111')
    match('.xxx.xxx.')
    match('...x...x...')

    no_match('')
    no_match('aaa')
    no_match('aba')
    no_match('abab')
    no_match('baba')
    no_match('12x12y12')
    no_match('abaca')
    no_match('1x2x3')
