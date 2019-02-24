from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import regex_test
from scripting.assertions import assert_truthy, assert_falsey


with regex_test('contains_no_a') as (match, no_match):
    match('')
    match('x')
    match('bqopvpod')

    no_match('a')
    no_match('xxxaxxxx')
    no_match('pppa')
