from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import reference_based_test
from scripting.reference import active_reference_implementation_from_id, reference_file


with reference_file('solution.py'):
    with reference_based_test('nth_longest_string') as testcase:
        testcase(1, [ 'a', 'bb', 'ccc', 'dddd' ])
        testcase(2, [ 'a', 'bb', 'ccc', 'dddd' ])
        testcase(3, [ 'a', 'bb', 'ccc', 'dddd' ])
        testcase(4, [ 'a', 'bb', 'ccc', 'dddd' ])
        testcase(1, [ 'bb', 'ccc', 'a', 'dddd' ])
        testcase(2, [ 'bb', 'ccc', 'a', 'dddd' ])
        testcase(3, [ 'bb', 'ccc', 'a', 'dddd' ])
        testcase(4, [ 'bb', 'ccc', 'a', 'dddd' ])

        for i in range(1, 10):
            testcase(i, [ 'x' * ((5 * k) % 17) for k in range(1, 17) ])
