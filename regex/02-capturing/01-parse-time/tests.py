from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import reference_based_test
from scripting.reference import active_reference_implementation_from_id, reference_file


with reference_file('solution.py'):
    with reference_based_test('parse_time') as testcase:
        testcase('00:00:00')
        testcase('12:34:56')
        testcase('12:34:56.000')
        testcase('12:34:56.001')
        testcase('12:34:56.491')
        testcase('')
        testcase('::')
        testcase('0:00:00')
        testcase('00:0:00')
        testcase('00:00:0')
        testcase('00:00:00.1')
        testcase('aa:bb:cc')

