from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import regex_test
from scripting.assertions import assert_truthy, assert_falsey


with regex_test('thrice_repeated') as (match, no_match):
    @test()
    def _():
        match('aaa')
        match('xxx')
        match('ababab')
        match('xyzxyzxyz')
        match('aaaaaaaaa')
        match('123456789123456789123456789')

        no_match('')
        no_match('a')
        no_match('aa')
        no_match('aab')
        no_match('aaab')
        no_match('xyzxyzxy')
