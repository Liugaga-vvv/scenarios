import sys

sys.path.append("/home/labex/project")

import unittest
from count_duplicates import count_duplicates

class TestCountDuplicates(unittest.TestCase):
    def test_count_duplicates(self):
        self.assertEqual(count_duplicates('abcde'), 0)
        self.assertEqual(count_duplicates('aabbcde'), 2)
        self.assertEqual(count_duplicates('aabBBcde'), 2)
        self.assertEqual(count_duplicates('indivisibility'), 1)


if __name__ == '__main__':
    unittest.main()
