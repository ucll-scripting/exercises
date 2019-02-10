from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import reference_based_test
from scripting.reference import active_reference_implementation_from_id, reference_file


with reference_file('solution.py'):
    with reference_based_test('drop_last') as testcase:
        testcase([ 1 ])
        testcase([ 1, 2 ])
        testcase([ 1, 2 ], n=2)
        testcase([ 2, 1 ])
        testcase([ 2, 1 ], n=2)
        testcase([ 4, 6, 1, 3, 2 ])
        testcase([ 4, 6, 1, 3, 2 ], n=2)
        testcase([ 4, 6, 1, 3, 2 ], n=3)
        testcase([ 4, 6, 1, 3, 2 ], n=4)
