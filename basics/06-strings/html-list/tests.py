from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import reference_based_test
from scripting.reference import active_reference_implementation_from_id, reference_file


with reference_file('solutions.py'):
    with reference_based_test('html_list') as testcase:
        testcase([])
        testcase(['a'])
        testcase(['a', 'b'])
        testcase(['a', 'b', 'c'])
        testcase(['x', 'yy', 'zzz'])
