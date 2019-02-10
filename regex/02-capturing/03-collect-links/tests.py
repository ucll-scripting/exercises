from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import reference_based_test
from scripting.reference import active_reference_implementation_from_id, reference_file


with reference_file('solution.py'):
    with reference_based_test('collect_links') as testcase:
        testcase('''
        <a href="a">fdf</a>
        fjklfjls
        <a href="b">qff</a>
        djqkljl
        <a href="abc">dfdg</a>
        fdjflkjdlf
        <a href="fiop">fdghh</a>
        ''')

