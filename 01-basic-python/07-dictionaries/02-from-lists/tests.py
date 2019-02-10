from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import reference_based_test
from scripting.reference import active_reference_implementation_from_id, reference_file


with reference_file('solution.py'):
    with reference_based_test('from_lists') as testcase:
        testcase([], [])
        testcase(['a'], [1])
        testcase(['a', 'b'], [1, 2])
        testcase([1, 2], ['a', 'b'])
        testcase([False, True], [4, 6])
