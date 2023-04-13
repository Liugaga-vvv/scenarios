import sys

sys.path.append("/home/labex/project")

import unittest
from find_expressions import find_expressions

class TestFindExpressions(unittest.TestCase):
    def test_find_expressions(self):
        nums = [1, 2, 3, 4]
        target = 5
        self.assertEqual(find_expressions(nums, target), ['1+4', '2+3'])
        nums = [2, 3, 4, 5]
        target = 8
        self.assertEqual(find_expressions(nums, target), ['2*4', '3+5'])
        nums = [2, 3, 4, 14]
        target = 7
        self.assertEqual(find_expressions(nums, target), ['14/2','3+4'])
        nums = [1, 2, 3, 4]
        target = 10
        self.assertEqual(find_expressions(nums, target), [])
        nums = [10, 20, 5, 2]
        target = 10
        self.assertEqual(find_expressions(nums, target), ['20-10', '20/2', '5*2'])
        nums = [10, 20, 5, 2, 6, 7, 8, 15, 25, 3]
        target = 10
        self.assertEqual(find_expressions(nums, target), ['20-10', '20/2', '5*2', '15-5', '2+8', '7+3', '25-15'])

if __name__ == '__main__':
    unittest.main()