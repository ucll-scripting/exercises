from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import reference_based_test
from scripting.reference import active_reference_implementation_from_id, reference_file
import os


with reference_file('solutions.py'):
    with reference_based_test('read_file') as _testcase:
        def testcase(filename, contents):
            with open(filename, 'w') as file:
                file.write(contents)
            _testcase(filename)
            os.remove(filename)

        testcase('a.temp', 'a')
        testcase('b.temp', 'bbb')
        testcase('c.temp', 'xxx')