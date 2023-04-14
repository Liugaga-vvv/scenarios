import unittest
from unittest.mock import patch
from io import StringIO
import sys

sys.path.append("/home/labex/project/")
import argparse
import greet

class TestGreet(unittest.TestCase):
    def test_greet_without_optional_argument(self):
        expected_output = "Hello, Alice!\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            sys.argv = ['greet.py', '--name', 'Alice']
            greet.main()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_greet_with_optional_argument(self):
        expected_output = "Hi there, Bob!\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            sys.argv = ['greet.py', '--name', 'Bob', '--greeting', 'Hi there']
            greet.main()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_greet_without_name_argument(self):
        expected_output = "error: the following arguments are required: --name\n"
        with patch('sys.stderr', new=StringIO()) as fake_err:
            sys.argv = ['greet.py', '--greeting', 'Hi there']
            with self.assertRaises(SystemExit):
                greet.main()
            self.assertIn(expected_output,fake_err.getvalue())

if __name__ == '__main__':
    unittest.main()