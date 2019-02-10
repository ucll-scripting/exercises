from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import reference_based_test
from scripting.reference import active_reference_implementation_from_id, reference_file


with reference_file('solution.py'):
    with reference_based_test('first') as testcase:
        testcase([1])
        testcase([2, 1])
        testcase([5, 2, 1])
        testcase([7, 1, 2, 1])
        testcase([8, 6, 2, 1])
        testcase([9, 6, 2, 1, 6])
