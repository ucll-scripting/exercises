from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import regex_test
from scripting.assertions import assert_truthy, assert_falsey


with regex_test('does_not_end_with_a') as (match, no_match):
    @test()
    def _():
        match('')
        match('k')
        match('ak')
        match('aaaak')

        no_match('a')
        no_match('bbba')
        no_match('ababa')
