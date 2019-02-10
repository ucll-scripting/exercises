from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import reference_based_test
from scripting.reference import active_reference_implementation_from_id, reference_file


with reference_file('solution.py'):
    with reference_based_test('make_path') as testcase:
        testcase([])
        testcase(['a'])
        testcase(['a', 'b'])
        testcase(['a', 'b', 'c'])
        testcase(['abc', '123', 'xyz'])
