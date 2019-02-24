from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import regex_test
from scripting.assertions import assert_truthy, assert_falsey


with regex_test('three_to_ten_times_abc') as (match, no_match):
    for i in range(3, 11):
        match('abc' * i)

    no_match('')
    no_match('a')
    no_match('ab')
    no_match('abc')
    no_match('abc' * 2)
    no_match('abc' * 11)
