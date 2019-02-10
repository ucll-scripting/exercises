from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import reference_based_test
from scripting.reference import active_reference_implementation_from_id, reference_file


with reference_file('solution.py'):
    with reference_based_test('drop_first') as testcase:
        testcase([1])
        testcase([1, 2])
        testcase([1, 2, 3])
        testcase([5, 2, 3])
        testcase([7, 1, 5, 3])
        testcase([7, 1, 7, 7])
