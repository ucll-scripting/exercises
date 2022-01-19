from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import reference_based_test
from scripting.reference import active_reference_implementation_from_id, reference_file


with reference_file('solution.py'):
    with reference_based_test('middle') as testcase:
        testcase([1])
        testcase([1, 2])
        testcase([1, 2, 3])
        testcase([1, 3, 2])
        testcase([3, 2, 1])
        testcase([2, 1, 3])
        testcase([1, 2, 3, 4])
        testcase([4, 2, 6, 5, 4, 1, 2, 7, 6, 4, 5])
        testcase([4, 2, 6, 5, 4, 1, 2, 7, 6, 4, 5, 9])
