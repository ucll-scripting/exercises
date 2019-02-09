from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import regex_test
from scripting.assertions import assert_truthy, assert_falsey


with regex_test('zero_or_more_abc') as (match, no_match):
    for i in range(0, 11):
        match('abc' * i)

    no_match('ab')
    no_match('abca')
