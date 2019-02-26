from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import regex_test
from scripting.assertions import assert_truthy, assert_falsey


with regex_test('is_valid_email_address') as (match, no_match):
    match('a.b@student.ucll.be')
    match('a.b@ucll.be')
    match('a@ucll.be')
    match('a.b.c@ucll.be')
    match('123@student.ucll.be')

    no_match('')
    no_match('a')
    no_match('a-b@ucll.be')
    no_match('ab@ucl.be')
    no_match('ab@ucll.com')
    no_match('@ucll.be')
    no_match('a.b@')
    no_match('xucll.be')
    no_match('a.b@ucllxbe')
    no_match('a.b@studentxucllxbe')
    no_match('a.b@student.ucll.bex')
    no_match('-a.b@student.ucll.be')
