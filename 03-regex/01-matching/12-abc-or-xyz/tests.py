from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import regex_test
from scripting.assertions import assert_truthy, assert_falsey


with regex_test('abc_or_xyz') as (match, no_match):
    match('abc')
    match('xyz')

    no_match('')
    no_match('a')
    no_match('ab')
    no_match('abca')
    no_match('x')
    no_match('xy')
    no_match('xyza')
    no_match('abcxyz')
