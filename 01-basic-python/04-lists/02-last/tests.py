from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import reference_based_test
from scripting.reference import active_reference_implementation_from_id, reference_file


with reference_file('solution.py'):
    with reference_based_test('last') as testcase:
        testcase([1])
        testcase([1, 2])
        testcase([1, 2, 3])
        testcase([1, 2, 4])
        testcase([1, 2, 4, 7, 6, 0])
