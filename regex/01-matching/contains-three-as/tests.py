from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import regex_test
from scripting.assertions import assert_truthy, assert_falsey


with regex_test('contains_three_as') as (match, no_match):
    @test()
    def _():
        match('aaa')
        match('axaa')
        match('axaxa')
        match('xaxaxa')
        match('xaxaxax')
        match('xaxxaxxxxax')

        no_match('')
        no_match('a')
        no_match('aa')
        no_match('axa')
