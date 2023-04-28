import sys

sys.path.append("/home/labex/project")
import unittest
from simple_calculator import simple_calculator


class TestStep2(unittest.TestCase):
    def test_valid_input(self):
        result1 = simple_calculator().validate_user_input("10", "5", "+")
        result2 = simple_calculator().validate_user_input("10", "5", "-")
        result3 = simple_calculator().validate_user_input("10", "5", "*")
        result4 = simple_calculator().validate_user_input("10", "5", "/")
        self.assertEqual(result1, None)
        self.assertEqual(result2, None)
        self.assertEqual(result3, None)
        self.assertEqual(result4, None)

    def test_invalid_input(self):
        result1 = simple_calculator().validate_user_input("abc", "def", "@")
        result2 = simple_calculator().validate_user_input("2", "3", "@")
        self.assertEqual(result1, "Please enter valid numbers")
        self.assertEqual(result2, "Please enter a valid operation")


if __name__ == "__main__":
    unittest.main()
