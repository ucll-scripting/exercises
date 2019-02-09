from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import regex_test
from scripting.assertions import assert_truthy, assert_falsey


with regex_test('only_digits') as (match, no_match):
    match('')
    match('0')
    match('1')
    match('2')
    match('3')
    match('4')
    match('5')
    match('6')
    match('7')
    match('8')
    match('9')
    match('1235020284')

    no_match('a')
    no_match('d')
    no_match('125f')
    no_match('78a3')
    no_match('q2100')
