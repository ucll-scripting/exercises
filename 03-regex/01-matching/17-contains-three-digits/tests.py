from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import regex_test
from scripting.assertions import assert_truthy, assert_falsey


with regex_test('contains_three_digits') as (match, no_match):
    match('123')
    match('8132')
    match('a813')
    match('813x')
    match('g813x')
    match('9x9x9')
    match('f8a1q3x')
    match('dddd787ddddd')

    no_match('')
    no_match('5')
    no_match('12')
    no_match('5q9f')
