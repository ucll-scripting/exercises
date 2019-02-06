from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import reference_based_test
from scripting.reference import active_reference_implementation_from_id, reference_file


with reference_file('solutions.py'):
    with reference_based_test('encode') as testcase:
        testcase({ }, '')
        testcase({ 'a': 'b' }, 'a')
        testcase({ 'a': 'b' }, 'aa')
        testcase({ 'a': 'c' }, 'aa')
        testcase({ 'a': 'c', 'b': 'a', 'c': 'b' }, 'abccab')
