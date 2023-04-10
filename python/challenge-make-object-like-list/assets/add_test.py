import sys

sys.path.append("/home/labex/project")
import unittest
from magic_list import MagicList


class TestMagicList(unittest.TestCase):
    def setUp(self):
        self.magic_list = MagicList(1, 2, 3)

    def test_add(self):
        result = self.magic_list + [4, 5, 6]
        self.assertEqual(result, [1, 2, 3, 4, 5, 6])

    def test_iadd(self):
        self.magic_list += [4, 5, 6]
        self.assertEqual(self.magic_list, [1, 2, 3, 4, 5, 6])


if __name__ == "__main__":
    unittest.main()
