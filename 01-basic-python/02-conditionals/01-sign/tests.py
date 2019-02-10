from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import reference_based_test
from scripting.reference import active_reference_implementation_from_id, reference_file


with reference_file('solution.py'):
    with reference_based_test('sign') as testcase:
        for x in [ 0, 1, 2, -5, -8 ]:
            testcase(x)