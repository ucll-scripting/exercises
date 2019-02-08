from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import reference_based_test
from scripting.reference import active_reference_implementation_from_id, reference_file


with reference_file('solutions.py'):
    with reference_based_test('pairwise_sum') as testcase:
        for i in range(0, 50):
            testcase([], [])
            testcase([0], [0])
            testcase([0], [1])
            testcase([1], [0])
            testcase([0, 0, 1], [0, 1, 0])
            testcase([1, 2, 3], [4, 5, 5])
            testcase([8, 4, 7], [5, 1, 6])
            testcase([8, 4, 7, 1], [5, 1, 6, 2])
