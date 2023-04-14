import sys

sys.path.append("/home/labex/project")
import unittest
from magic_list import MagicList


class TestMagicList(unittest.TestCase):
    def setUp(self):
        self.magic_list = MagicList(3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5)

    def test_sub(self):
        result = self.magic_list - [5, 3]
        self.assertEqual(result, [1, 4, 1, 9, 2, 6])

    def test_mul(self):
        result = self.magic_list * 2
        self.assertEqual(
            result, [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        )


if __name__ == "__main__":
    unittest.main()
