from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import reference_based_test
from scripting.reference import active_reference_implementation_from_id, reference_file


with reference_file('solution.py'):
    with reference_based_test('count_turns') as testcase:
        testcase([])
        testcase([1])
        testcase([1, 1])
        testcase([1, 2])
        testcase([1, 2, 3])
        testcase([1, 2, 1])
        testcase([1, 2, 5, 3])
        testcase([5, 7, 6, 1, 2, 4, 6, 7, 9, 7, 3, 2, 4, 6])
