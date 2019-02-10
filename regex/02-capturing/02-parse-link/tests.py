from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import reference_based_test
from scripting.reference import active_reference_implementation_from_id, reference_file


with reference_file('solution.py'):
    with reference_based_test('parse_link') as testcase:
        testcase('<a href="xxx">lalala</a>')
        testcase('<a href="ajflk">iojfgkld</a>')
        testcase('<a href="xxx">lalala')
        testcase('href="xxx">lalala<')

