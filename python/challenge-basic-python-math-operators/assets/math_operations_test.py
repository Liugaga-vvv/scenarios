import sys

sys.path.append("/home/labex/project")
import unittest
from math_operations import basic_math_operations


class TestBasicMathOperations(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(
            basic_math_operations(3, 5).split("\n")[0], "The sum of 3 and 5 is 8."
        )

    def test_difference(self):
        self.assertEqual(
            basic_math_operations(7, 4).split("\n")[1],
            "The difference between 7 and 4 is 3.",
        )

    def test_product(self):
        self.assertEqual(
            basic_math_operations(-2, 6).split("\n")[2],
            "The product of -2 and 6 is -12.",
        )

    def test_quotient(self):
        self.assertEqual(
            basic_math_operations(15, 3).split("\n")[3],
            "The quotient of 15 and 3 is 5.0.",
        )

    def test_remainder(self):
        self.assertEqual(
            basic_math_operations(10, 3).split("\n")[4],
            "The remainder when 10 is divided by 3 is 1.",
        )


if __name__ == "__main__":
    unittest.main()
