import sys

sys.path.append("/home/labex/project/")

import unittest
from basic_syntax import basic_syntax


class TestAssignmentExpressionsChallenge(unittest.TestCase):
    def test_basic_assignment_expression(self):
        self.assertEqual(basic_syntax(), 42)


if __name__ == "__main__":
    unittest.main()
