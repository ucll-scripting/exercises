from contextlib import contextmanager
from scripting.testing import test
from scripting.tested import active_tested_implementation_from_id, current_active_tested_implementation
from scripting.assertions import assert_truthy, assert_falsey
import re



@contextmanager
def problem(id):
    with active_tested_implementation_from_id(id):
        yield


def match(string):
    f = current_active_tested_implementation()
    assert_truthy(f(string), message=f"'{string}' should match regex")

def no_match(string):
    f = current_active_tested_implementation()
    assert_falsey(f(string), message=f"'{string}' should not match regex")


with problem('equals_a'):
    @test()
    def _():
        match('a')

        no_match('b')
        no_match('')
        no_match('aa')


with problem('starts_with_a'):
    @test()
    def _():
        match('a')
        match('ab')
        match('abc')
        match('aaaa')

        no_match('')
        no_match('b')
        no_match('xaa')


with problem('contains_a'):
    @test()
    def _():
        match('a')
        match('ab')
        match('aaaa')
        match('xax')
        match('xxaa')

        no_match('')
        no_match('b')


with problem('ends_with_a'):
    @test()
    def _():
        match('a')
        match('ba')
        match('cba')
        match('aaaa')

        no_match('')
        no_match('b')
        no_match('ax')


with problem('contains_no_a'):
    @test()
    def _():
        match('')
        match('x')
        match('bqopvpod')

        no_match('a')
        no_match('xxxaxxxx')
        no_match('pppa')


with problem('does_not_start_with_a'):
    @test()
    def _():
        match('')
        match('k')
        match('ka')
        match('kaaaa')

        no_match('a')
        no_match('abbb')
        no_match('ababa')


with problem('does_not_end_with_a'):
    @test()
    def _():
        match('')
        match('k')
        match('ak')
        match('aaaak')

        no_match('a')
        no_match('bbba')
        no_match('ababa')

with problem('contains_three_as'):
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
