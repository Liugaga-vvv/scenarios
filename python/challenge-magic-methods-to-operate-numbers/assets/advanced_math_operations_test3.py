import unittest
import sys

sys.path.append("/home/labex/project")

from advanced_math_operations import MathExpression


class TestMathExpression(unittest.TestCase):
    def test_floordiv(self):
        a = MathExpression(5)
        b = MathExpression(7)
        c = b // a
        self.assertEqual(str(c), "1")


if __name__ == "__main__":
    unittest.main()
