import sys

sys.path.append("/home/labex/project")
import unittest
from magic_list import MagicList


class TestMagicList(unittest.TestCase):
    def setUp(self):
        self.magic_list = MagicList(3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5)

    def test_lt(self):
        other = MagicList(3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 6)
        self.assertTrue(self.magic_list < other)
        other = MagicList(3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5)
        self.assertFalse(self.magic_list < other)

    def test_sort(self):
        self.magic_list.sort()
        self.assertEqual(self.magic_list._data, [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])


if __name__ == "__main__":
    unittest.main()
