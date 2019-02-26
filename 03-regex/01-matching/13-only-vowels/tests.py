from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import regex_test
from scripting.assertions import assert_truthy, assert_falsey


with regex_test('only_vowels') as (match, no_match):
    match('')
    match('a')
    match('e')
    match('i')
    match('o')
    match('u')
    match('aeiou')
    match('eioaauie')

    no_match('x')
    no_match('ab')
    no_match('aiop')
    no_match('xooo')
