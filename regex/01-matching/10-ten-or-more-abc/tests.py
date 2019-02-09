from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import regex_test
from scripting.assertions import assert_truthy, assert_falsey


with regex_test('ten_or_more_abc') as (match, no_match):
    match('abc' * 10)
    match('abc' * 11)
    match('abc' * 12)
    match('abc' * 13)
    match('abc' * 14)

    no_match('')
    no_match('a')
    no_match('ab')
    no_match('abc')
    no_match('abc' * 9)
