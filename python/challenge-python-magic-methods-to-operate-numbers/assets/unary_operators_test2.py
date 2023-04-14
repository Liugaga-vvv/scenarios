import unittest
import sys

sys.path.append("/home/labex/project")

from unary_operators import MathExpression


class TestMathExpression(unittest.TestCase):
    def test_pos(self):
        a = MathExpression(-5)
        b = +a
        self.assertEqual(str(b), "5")


if __name__ == "__main__":
    unittest.main()
