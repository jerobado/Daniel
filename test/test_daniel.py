import unittest
import os
import random
import string

from src.core import daniel


class DanielCoreTest(unittest.TestCase):
    """ Test core operations of Daniel -> daniel.py """

    def test_create_email(self):

        sender = 'tokidokitalkyou@gmail.com'
        recipient = 'tokidokitalkyou@gmail.com'
        subject = 'xxx'
        message = 'xxxxxxxxxxxxx'

        result = daniel.create_email(sender, recipient, subject, message)
        self.assertIsInstance(result, type(result))

    def test_save_email(self):

        sender = 'tokidokitalkyou@gmail.com'
        recipient = 'tokidokitalkyou@gmail.com'
        subject = 'test save_email method'
        message = 'is the email created?'

        email = daniel.create_email(sender, recipient, subject, message)

        suffix = ''.join([random.choice(string.digits) for index in range(4)])
        # filename = f'test_email{suffix}.eml'
        filename = f'test_email.eml'

        daniel.save_email(email, filename)
        check_filename = os.path.exists(filename)

        test_message = f'\'{filename}\' not found in {os.getcwd()}'
        self.assertTrue(check_filename, test_message)


if __name__ == '__main__':
    unittest.main()
