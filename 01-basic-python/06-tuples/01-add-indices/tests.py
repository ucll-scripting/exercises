from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import reference_based_test
from scripting.reference import active_reference_implementation_from_id, reference_file


with reference_file('solution.py'):
    with reference_based_test('add_indices') as testcase:
        testcase([])
        testcase([1])
        testcase([1, 2])
        testcase([1, 1])
        testcase([1, 2, 3])
        testcase([1, 4, 5, 7])
        testcase([4, 1])
        testcase([4, 5, 8, 2, 4, 6])
        testcase([*"abcde"])
