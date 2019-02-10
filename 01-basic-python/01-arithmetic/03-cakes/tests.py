from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import reference_based_test
from scripting.reference import active_reference_implementation_from_id, reference_file


with reference_file('solution.py'):
    with reference_based_test('cakes') as testcase:
        testcase(0, 0, 0)
        testcase(10, 0, 0)
        testcase(10, 250, 0)
        testcase(10, 250, 250)
        testcase(10, 250, 500)
        testcase(10, 1000, 500)
        testcase(18, 1000, 800)