from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import regex_test
from scripting.assertions import assert_truthy, assert_falsey


with regex_test('is_dna') as (match, no_match):
    match('')
    match('G')
    match('A')
    match('T')
    match('C')
    match('CGAT')
    match('GCCTATAGTAGACG')
    match('CCCCGGGGAAAATTTT')

    no_match('a')
    no_match('g')
    no_match('c')
    no_match('t')
    no_match('q')
    no_match('Q')
    no_match('PGATCCCC')
