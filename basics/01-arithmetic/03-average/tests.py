from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import reference_based_test
from scripting.reference import active_reference_implementation_from_id, reference_file


with reference_file('solutions.py'):
    with reference_based_test('average') as testcase:
        testcase(0, 0)
        testcase(0, 2)
        testcase(0, 4)
        testcase(1, 3)
        testcase(10, 20)
        testcase(0, 1)