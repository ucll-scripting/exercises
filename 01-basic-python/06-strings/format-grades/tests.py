from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import reference_based_test
from scripting.reference import active_reference_implementation_from_id, reference_file


with reference_file('solutions.py'):
    with reference_based_test('format_grades') as testcase:
        testcase([])
        testcase([('John', 14)])
        testcase([('John', 12), ('Ann', 15)])
        testcase([('John', 12), ('Ann', 15), ('Steven', 8)])
