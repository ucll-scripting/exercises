from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import reference_based_test
from scripting.reference import active_reference_implementation_from_id, reference_file


with reference_file('solution.py'):
    with reference_based_test('scrape_email_addresses') as testcase:
        testcase('''
        a@c.com
        ''')

        testcase('''
        111@AFF.com
        ''')

        testcase('''
        111@AFF.com
        ''')

        testcase('''
        a@c.com fsjdf jfslk fkls fjl df
        jalfkj b@d.be fjdlkf jfkljdlkf
        qpoiopc fdfqpof ifppopo fkpqo
        qfjlkl xyz@ppp.fr jkfljqlkj
        ''')

