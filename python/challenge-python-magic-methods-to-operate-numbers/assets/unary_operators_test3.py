import unittest
import sys

sys.path.append("/home/labex/project")

from unary_operators import MathExpression


class TestMathExpression(unittest.TestCase):
    def test_abs(self):
        a = MathExpression(-5)
        b = abs(a)
        self.assertEqual(str(b), "5")


if __name__ == "__main__":
    unittest.main()
