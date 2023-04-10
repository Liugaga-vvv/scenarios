import unittest
import sys

sys.path.append("/home/labex/project")

from basic_math_operations import MathExpression


class TestMathExpression(unittest.TestCase):
    def test_sub(self):
        a = MathExpression(5)
        b = MathExpression(7)
        c = b - a
        self.assertEqual(str(c), "2")


if __name__ == "__main__":
    unittest.main()
