from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import reference_based_test
from scripting.reference import active_reference_implementation_from_id, reference_file


with reference_file('solution.py'):
    with reference_based_test('coins') as testcase:
        testcase(0, 0, 0, 0)
        testcase(0, 0, 0, 1)
        testcase(1, 0, 0, 1)
        testcase(1, 0, 0, 2)
        testcase(2, 0, 0, 2)
        testcase(0, 1, 0, 2)
        testcase(0, 1, 0, 5)
        testcase(0, 0, 1, 5)
        testcase(2, 0, 1, 5)
        testcase(2, 0, 1, 6)
        testcase(2, 0, 1, 7)
        testcase(2, 0, 1, 8)
        testcase(2, 1, 1, 8)
        testcase(0, 0, 1, 4)
        testcase(0, 1, 1, 6)