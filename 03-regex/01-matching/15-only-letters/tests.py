from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import regex_test
from scripting.assertions import assert_truthy, assert_falsey


with regex_test('only_letters') as (match, no_match):
    match('')
    match('a')
    match('P')
    match('fPczLO')

    no_match('7')
    no_match('d5')
    no_match('4012f78')
