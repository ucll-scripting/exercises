from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import regex_test
from scripting.assertions import assert_truthy, assert_falsey


with regex_test('equals_a') as (match, no_match):
    @test()
    def _():
        match('a')

        no_match('b')
        no_match('')
        no_match('aa')
