from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import reference_based_test
from scripting.reference import active_reference_implementation_from_id, reference_file


with reference_file('solution.py'):
    with reference_based_test('all_greater') as testcase:
        testcase([], [])
        testcase([1], [])
        testcase([], [1])
        testcase([2], [1])
        testcase([1], [2])
        testcase([5, 7, 8], [4, 2, 1])
        testcase([5, 7, 8, 3], [4, 2, 1])
