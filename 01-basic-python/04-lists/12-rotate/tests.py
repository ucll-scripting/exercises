from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import reference_based_test
from scripting.reference import active_reference_implementation_from_id, reference_file


with reference_file('solution.py'):
    with reference_based_test('rotate') as testcase:
        for i in range(1, 10):
            testcase([1], i)
            testcase([1, 2], i)
            testcase([1, 2, 3, 4, 5], i)
            testcase([*"abcdefgh"], i)
