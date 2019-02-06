from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import reference_based_test
from scripting.reference import active_reference_implementation_from_id, reference_file


with reference_file('solutions.py'):
    with reference_based_test('manhattan') as testcase:
        testcase((0, 0), (0, 0))
        testcase((0, 0), (5, 0))
        testcase((0, 0), (0, 3))
        testcase((0, 0), (5, 3))
        testcase((1, 1), (5, 3))
        testcase((1, 2), (7, 2))
        testcase((7, 5), (2, 3))
