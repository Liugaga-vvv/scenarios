import unittest
import sys

sys.path.append("/home/labex/project")

from comparisons import MathExpression


class TestMathExpression(unittest.TestCase):
    def test_lt(self):
        a = MathExpression(5)
        b = MathExpression(7)
        self.assertTrue(a < b)


if __name__ == "__main__":
    unittest.main()
