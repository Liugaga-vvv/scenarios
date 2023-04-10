import sys

sys.path.append("/home/labex/project/")

import unittest
from list_comprehension import list_comprehension


class TestAssignmentExpressionsChallenge(unittest.TestCase):
    def test_assignment_expression_in_list_comprehension(self):
        expected_result = [4, 16, 36, 64, 100]
        self.assertEqual(list_comprehension(), expected_result)


if __name__ == "__main__":
    unittest.main()
