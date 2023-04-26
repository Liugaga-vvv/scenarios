import unittest
import sys

sys.path.append("/home/labex/project")

from in_place_operations import MathExpression


class TestMathExpression(unittest.TestCase):
    def test_mul(self):
        a = MathExpression(5)
        b = MathExpression(7)
        a *= b
        self.assertEqual(str(a), "35")


if __name__ == "__main__":
    unittest.main()
