from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import reference_based_test
from scripting.reference import active_reference_implementation_from_id, reference_file


with reference_file('solution.py'):
    with reference_based_test('remove_repeated_words') as testcase:
        testcase('')
        testcase('a')
        testcase('aa')
        testcase('aa aa')
        testcase('aa a')
        testcase('a a b b')
        testcase('aaa aaa bb bb c c')
        testcase('a b a b')
        testcase('a a a a b')

