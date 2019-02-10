from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import reference_based_test
from scripting.reference import active_reference_implementation_from_id, reference_file


with reference_file('solution.py'):
    with reference_based_test('slug') as testcase:
        testcase('Prince')
        testcase('Tony Hoare')
        testcase('Dennis Ritchie')
        testcase('Guido van Rossum')
        testcase('Simon Peyton Jones')
        testcase('John Wilkes Booth')
