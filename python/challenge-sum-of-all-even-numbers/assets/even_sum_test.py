import sys

sys.path.append("/home/labex/project")

import unittest
from even_sum import even_sum

class TestEvenSum(unittest.TestCase):
    def test_even_sum(self):
        self.assertEqual(even_sum([1, 2, 3, 4, 5, 6]), 12)
        self.assertEqual(even_sum([10, 15, 20]), 30)
        self.assertEqual(even_sum([3, 5, 7]), 0)
        self.assertEqual(even_sum([]), 0)

if __name__ == '__main__':
    unittest.main()