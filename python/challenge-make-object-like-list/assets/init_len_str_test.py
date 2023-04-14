import sys

sys.path.append("/home/labex/project")
import unittest
from magic_list import MagicList


class TestMagicList(unittest.TestCase):
    def setUp(self):
        self.magic_list = MagicList(1, 2, 3)

    def test_init(self):
        self.assertEqual(self.magic_list._data, [1, 2, 3])

    def test_len(self):
        self.assertEqual(len(self.magic_list), 3)

    def test_str(self):
        self.assertEqual(str(self.magic_list), "[1, 2, 3]")

    def test_contains(self):
        self.assertTrue(1 in self.magic_list)
        self.assertTrue(2 in self.magic_list)
        self.assertTrue(3 in self.magic_list)
        self.assertFalse(4 in self.magic_list)


if __name__ == "__main__":
    unittest.main()
