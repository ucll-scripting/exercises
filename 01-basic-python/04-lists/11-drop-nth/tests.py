from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import reference_based_test
from scripting.reference import active_reference_implementation_from_id, reference_file


with reference_file('solution.py'):
    with reference_based_test('drop_nth') as testcase:
        testcase([1], 0)
        testcase([1, 2], 0)
        testcase([1, 2], 1)
        testcase([1, 2, 3], 0)
        testcase([1, 2, 3], 1)
        testcase([1, 2, 3], 2)
        testcase(['a', 'b', 'c', 'd', 'e'], 0)
        testcase(['a', 'b', 'c', 'd', 'e'], 1)
        testcase(['a', 'b', 'c', 'd', 'e'], 2)
        testcase(['a', 'b', 'c', 'd', 'e'], 3)
        testcase(['a', 'b', 'c', 'd', 'e'], 4)
