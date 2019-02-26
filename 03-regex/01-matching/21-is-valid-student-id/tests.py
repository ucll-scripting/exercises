from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import regex_test
from scripting.assertions import assert_truthy, assert_falsey


with regex_test('is_valid_student_id') as (match, no_match):
    match('r1234567')
    match('R1234567')
    match('s1234567')
    match('S1234567')
    match('r0000000')

    no_match('t1234567')
    no_match('1234567')
    no_match('r134567')
    no_match('r12345678')
    no_match('xr1234567')
    no_match('r1234567x')
