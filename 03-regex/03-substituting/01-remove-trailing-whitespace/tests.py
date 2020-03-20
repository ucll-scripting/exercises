from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import reference_based_test
from scripting.reference import active_reference_implementation_from_id, reference_file


with reference_file('solution.py'):
    with reference_based_test('remove_trailing_whitespace') as testcase:
        testcase('fdjfkld jfjs fjdslfk'.strip())
        testcase('fdjfkld jfjs fjdslfk ')
        testcase('fdjfkld jfjs fjdslfk\t')
        testcase('fdjfkld jfjs fjdslfk       ')
        testcase('x  \ny   ')

        testcase('''
        fdf qqip saofp k\x20\t\x20
        fjdklfj f sfjslkf\x20\x20\x20\x20\x20\x20
        fdjfkldjf\x20\x20''')

