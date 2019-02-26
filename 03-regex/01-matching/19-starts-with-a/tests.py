from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import regex_test
from scripting.assertions import assert_truthy, assert_falsey


with regex_test('starts_with_a') as (match, no_match):
    match('a')
    match('ab')
    match('aaaa')
    match('ax')

    no_match('')
    no_match('b')
    no_match('ga')
    no_match('xxaa')
