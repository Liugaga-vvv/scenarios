import sys

sys.path.append("/home/labex/project")
import unittest
from simple_calculator import simple_calculator


class TestStep3(unittest.TestCase):
    def test_addition(self):
        result = simple_calculator().perform_calculation(10, 5, "+")
        self.assertEqual(result, 15.0)

    def test_subtraction(self):
        result = simple_calculator().perform_calculation(10, 5, "-")
        self.assertEqual(result, 5.0)

    def test_multiplication(self):
        result = simple_calculator().perform_calculation(10, 5, "*")
        self.assertEqual(result, 50.0)

    def test_division(self):
        result = simple_calculator().perform_calculation(10, 5, "/")
        self.assertEqual(result, 2.0)


if __name__ == "__main__":
    unittest.main()
