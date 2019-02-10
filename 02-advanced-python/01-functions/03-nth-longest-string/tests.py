from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import reference_based_test
from scripting.reference import active_reference_implementation_from_id, reference_file


with reference_file('solution.py'):
    with reference_based_test('longest_string') as testcase:
        testcase([ '' ])
        testcase([ 'a' ])
        testcase([ 'a', '' ])
        testcase([ '', 'a' ])
        testcase([ 'a', 'b' ])
        testcase([ 'a', 'bb' ])
        testcase([ 'aa', 'b' ])
        testcase([ 'aaa', 'bbbb', 'cc', 'd' ])
        testcase([ 'aaa', 'bbbb', 'cc', 'ddddd' ])
        testcase([ 'aaa', 'bbbb', 'cccccccc', 'ddddd' ])
