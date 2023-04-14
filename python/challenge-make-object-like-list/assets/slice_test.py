import sys

sys.path.append("/home/labex/project")
import unittest
from magic_list import MagicList


class TestMagicList(unittest.TestCase):
    def setUp(self):
        self.magic_list = MagicList(1, 2, 3)

    def test_getitem(self):
        self.assertEqual(self.magic_list[0], 1)
        self.assertEqual(self.magic_list[1], 2)
        self.assertEqual(self.magic_list[2], 3)
        self.assertEqual(self.magic_list[0:2], [1, 2])
        self.assertEqual(self.magic_list[0:3:2], [1, 3])

    def test_setitem(self):
        self.magic_list[0] = 4
        self.assertEqual(self.magic_list[0], 4)
        self.magic_list[1:3] = [5, 6]
        self.assertEqual(self.magic_list[1], 5)
        self.assertEqual(self.magic_list[2], 6)


if __name__ == "__main__":
    unittest.main()
