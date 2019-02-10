from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import reference_based_test
from scripting.reference import active_reference_implementation_from_id, reference_file


with reference_file('solution.py'):
    with reference_based_test('format_grades') as testcase:
        testcase({})
        testcase({ 'John': [12] })
        testcase({ 'John': [12, 14] })
        testcase({ 'John': [12, 12, 13] })
        testcase({ 'John': [12, 13, 13] })
        testcase({ 'John': [12, 13, 13], 'Ann': [14, 11, 19] })
        testcase({ 'John': [17, 11, 8], 'Ann': [13, 10, 10], 'Robert': [13, 15, 9, 14] })
