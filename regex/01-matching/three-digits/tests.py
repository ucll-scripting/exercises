from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import regex_test
from scripting.assertions import assert_truthy, assert_falsey


with regex_test('three_digits') as (match, no_match):
    @test()
    def _():
        match('000')
        match('123')
        match('497')
        match('568')

        no_match('')
        no_match('1')
        no_match('12')
        no_match('1234')
        no_match('aaa')
        no_match('41p')
