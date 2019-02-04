from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import regex_test
from scripting.assertions import assert_truthy, assert_falsey


with regex_test('ends_with_a') as (match, no_match):
    @test()
    def _():
        match('a')
        match('ba')
        match('cba')
        match('aaaa')

        no_match('')
        no_match('b')
        no_match('ax')
