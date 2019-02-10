from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import reference_based_test
from scripting.reference import active_reference_implementation_from_id, reference_file


with reference_file('solution.py'):
    with reference_based_test('card_value') as testcase:
        for x in [ 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Ace', 'Jack', 'Queen', 'King' ]:
            testcase(x)