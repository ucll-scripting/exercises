from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import reference_based_test
from scripting.reference import active_reference_implementation_from_id, reference_file


with reference_file('solution.py'):
    with reference_based_test('between') as testcase:
        testcase(5, 0, 10)
        testcase(1, 1, 2)
        testcase(5, 1, 2)
        testcase(2, 3, 8)