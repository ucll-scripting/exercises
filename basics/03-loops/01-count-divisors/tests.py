from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import reference_based_test
from scripting.reference import active_reference_implementation_from_id, reference_file


with reference_file('solutions.py'):
    with reference_based_test('count_divisors') as testcase:
        for x in [ 5, 10, 12, 2 * 2 * 3 * 5 * 7 ]:
            testcase(x)
