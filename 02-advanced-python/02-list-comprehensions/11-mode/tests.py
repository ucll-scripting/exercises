from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import reference_based_test
from scripting.reference import active_reference_implementation_from_id, reference_file


with reference_file('solution.py'):
    with reference_based_test('mode') as testcase:
        testcase([1])
        testcase([1, 1])
        testcase([1, 1, 2])
        testcase([1, 2, 2])
        testcase([1, 2, 1])
        testcase([5, 2, 5])
        testcase([1, 2, 1, 3, 3, 3])
        testcase([6, 2, 6, 3, 6, 3])
        testcase([1] * 50000 + [2] * 49999)
