from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import regex_test
from scripting.assertions import assert_truthy, assert_falsey


with regex_test('is_valid_time') as (match, no_match):
    match('00:00:00')
    match('00:00:00.000')
    match('12:34:56.789')

    no_match('')
    no_match('0:00:00')
    no_match('00:0:00')
    no_match('00:00:0')
    no_match('00:00:00:000')
    no_match('aa:aa:aa')
