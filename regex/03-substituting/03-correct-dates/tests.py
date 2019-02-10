from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import reference_based_test
from scripting.reference import active_reference_implementation_from_id, reference_file


with reference_file('solution.py'):
    with reference_based_test('correct_dates') as testcase:
        testcase('1/2/3')
        testcase('12/11/2019')
        testcase('12/11/2019 6/7/1899')
        testcase('12/11/2019 fjklfjl 6/7/1899')
