from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import reference_based_test
from scripting.reference import active_reference_implementation_from_id, reference_file


with reference_file('solution.py'):
    with reference_based_test('target_sum') as testcase:
        testcase([], 10)
        testcase([1, 2, 3, 4], 10)
        testcase([1, 2, 3, 4], 2)
        testcase([1, 2, 3, 4], 3)
        testcase([1, 2, 3, 4], 5)
        testcase([1, 2, 3, 4], 8)
        testcase([4, 7, 19], 20)
        testcase([4, 7, 19], 23)
        testcase([4, 7, 19], 26)
