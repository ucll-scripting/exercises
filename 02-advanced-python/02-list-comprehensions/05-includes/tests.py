from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import reference_based_test
from scripting.reference import active_reference_implementation_from_id, reference_file


with reference_file('solution.py'):
    with reference_based_test('includes') as testcase:
        testcase([], [])
        testcase([2], [])
        testcase([2], [2])
        testcase([2], [1])
        testcase([1, 2, 3, 4], [1])
        testcase([1, 2, 3, 4], [1, 2])
        testcase([1, 2, 3, 4], [1, 2, 3])
        testcase([1, 2, 3, 4], [1, 2, 3, 4])
        testcase([1, 2, 3, 4], [4, 1])
        testcase([1, 2, 3, 4], [4, 4, 4, 4])
