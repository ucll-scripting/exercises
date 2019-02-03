from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import regex_test
from scripting.assertions import assert_truthy, assert_falsey


with regex_test('three_letters') as (match, no_match):
    @test()
    def _():
        match('aaa')
        match('AAA')
        match('abc')
        match('xyz')
        match('AoJ')

        no_match('')
        no_match('a')
        no_match('ap')
        no_match('apFK')
        no_match('123')
