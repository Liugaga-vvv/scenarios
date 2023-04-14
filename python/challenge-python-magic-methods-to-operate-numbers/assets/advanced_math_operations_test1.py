import unittest
import sys

sys.path.append("/home/labex/project")

from advanced_math_operations import MathExpression


class TestMathExpression(unittest.TestCase):
    def test_pow(self):
        a = MathExpression(5)
        b = MathExpression(7)
        c = a**b
        self.assertEqual(str(c), "78125")


if __name__ == "__main__":
    unittest.main()
