from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import reference_based_test
from scripting.reference import active_reference_implementation_from_id, reference_file
from scripting.assertions import assert_equal
from scripting.tested import fetch_tested_implementation
from scripting.scoring import scale, all_or_nothing
import os


def testcase(filename, data):
    tested = fetch_tested_implementation('write_file')

    @test()
    def _():
        tested(filename, data)

        with open(filename, 'r') as file:
            expected = file.read()
            assert_equal(expected=data, actual=expected)

        os.remove(filename)


with scale(1), all_or_nothing():
    testcase('a.temp', 'a')
    testcase('b.temp', 'xxxx')
    testcase('ccc.temp', 'fqjkll')