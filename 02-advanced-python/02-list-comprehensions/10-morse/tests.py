from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import reference_based_test
from scripting.reference import active_reference_implementation_from_id, reference_file


with reference_file('solution.py'):
    with reference_based_test('to_morse') as testcase:
        testcase('A')
        testcase('B')
        testcase('C')
        testcase('D')
        testcase('E')
        testcase('F')
        testcase('G')
        testcase('H')
        testcase('I')
        testcase('J')
        testcase('K')
        testcase('L')
        testcase('M')
        testcase('N')
        testcase('O')
        testcase('P')
        testcase('Q')
        testcase('R')
        testcase('S')
        testcase('T')
        testcase('U')
        testcase('V')
        testcase('W')
        testcase('X')
        testcase('Y')
        testcase('Z')
        testcase('a')
        testcase('g')
        testcase('ABCDEF')
        testcase('A B C D E F')
        testcase('MORSE CODE')

    with reference_based_test('from_morse') as testcase:
        testcase('.')
        testcase('...')
        testcase('---')
        testcase('. . --- -')
        testcase('. . .   --- .. -.   ... -.-')