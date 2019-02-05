from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import regex_test
from scripting.assertions import assert_truthy, assert_falsey


with regex_test('thrice_repeated') as (match, no_match):
    @test()
    def _():
        match('aaa')
        match('xxx')
        match('111')
        match('...')

        no_match('')
        no_match('a')
        no_match('aa')
        no_match('aab')
        no_match('aaax')
        no_match('xaaa')
