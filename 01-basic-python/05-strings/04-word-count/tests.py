from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import reference_based_test
from scripting.reference import active_reference_implementation_from_id, reference_file


with reference_file('solution.py'):
    with reference_based_test('word_count') as testcase:
        testcase('a')
        testcase('a b')
        testcase('a a')
        testcase('a aa')
        testcase('a aa aaa')
        testcase('x x x x x')
