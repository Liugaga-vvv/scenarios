import unittest
import sys

sys.path.append("/home/labex/project")

from in_place_operations import MathExpression


class TestMathExpression(unittest.TestCase):
    def test_truediv(self):
        a = MathExpression(5)
        b = MathExpression(7)
        b /= a
        self.assertEqual(str(b), "1.4")


if __name__ == "__main__":
    unittest.main()
