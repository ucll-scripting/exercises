from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import regex_test
from scripting.assertions import assert_truthy, assert_falsey


with regex_test('is_valid_password') as (match, _no_match):
    def no_match(string, reason):
        _no_match(string, f"'{string}' should be rejected: {reason}")

    match('aA1+oipa')
    match('7Af9xf*6')
    match('Fpq75s.4+')

    no_match('aA1+', 'too short')
    no_match('aA1+fqx', 'too short')
    no_match('a19+fqios', 'does not contain an uppercase letter')
    no_match('-13AG1PA', 'does not contain a lowercase letter')
    no_match('aOO+fqios', 'does not contain a digit')
    no_match('aOO9fq5os', 'does not contain special symbol')
    no_match('aaa12+Fk', 'three consecutive times a')
    no_match('Lf8xxx12+Fk', 'three consecutive times x')
    no_match('A.A7AaA', 'four times A')