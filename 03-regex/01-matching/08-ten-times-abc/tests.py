from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import regex_test
from scripting.assertions import assert_truthy, assert_falsey


with regex_test('ten_times_abc') as (match, no_match):
    match('abc' * 10)

    no_match('')
    no_match('a')
    no_match('ab')
    no_match('abc')
    no_match('abc' * 9)
    no_match('abc' * 11)
    no_match('abc' * 12)
    no_match('abc' * 13)
    no_match('abc' * 14)
