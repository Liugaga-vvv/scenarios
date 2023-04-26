import sys

sys.path.append("/home/labex/project")
import unittest
from io import StringIO
from unittest.mock import patch
from simple_calculator import simple_calculator


def run_simple_calculator(num1, num2, operation):
    with patch("sys.stdout", new=StringIO()) as fake_out:
        with patch("builtins.input", side_effect=[num1, num2, operation]):
            simple_calculator()
    return fake_out.getvalue().strip()


class TestStep1(unittest.TestCase):
    def test_input_numbers_and_operation(self):
        calculator = simple_calculator()
        with patch("builtins.input", side_effect=["10", "5", "+"]):
            num1, num2, operation = calculator.get_user_input()
        self.assertEqual(num1, "10")
        self.assertEqual(num2, "5")
        self.assertEqual(operation, "+")


if __name__ == "__main__":
    unittest.main()
