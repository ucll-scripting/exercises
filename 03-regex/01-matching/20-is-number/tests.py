from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import regex_test
from scripting.assertions import assert_truthy, assert_falsey


with regex_test('is_number') as (match, no_match):
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
    match('0.1')
    match('3.141592')
    match('1980')

    no_match('')
    no_match('.')
    no_match('.0')
    no_match('0.')
    no_match('b')
    no_match('1.2.3')
    no_match('1,2')
