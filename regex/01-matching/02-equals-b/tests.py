from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import regex_test
from scripting.assertions import assert_truthy, assert_falsey


with regex_test('equals_b') as (match, no_match):
    match('b')

    no_match('a')
    no_match('')
    no_match('bb')
