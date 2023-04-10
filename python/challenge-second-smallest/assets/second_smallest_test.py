import sys

sys.path.append("/home/labex/project")

import unittest
from second_smallest import second_smallest


class SecondSmallestTestCase(unittest.TestCase):
    def test_second_smallest(self):
        self.assertEqual(second_smallest([1, 2, 3, 4, 5]), 2)
        self.assertEqual(second_smallest([5, 4, 3, 2, 1]), 2)
        self.assertEqual(second_smallest([1]), None)
        self.assertEqual(second_smallest([7, 7, 7]), 7)
        self.assertEqual(second_smallest([-5, -4, -3, -2, -1]), -4)


if __name__ == "__main__":
    unittest.main()
