import sys

sys.path.append("/home/labex/project/")

import unittest
from magic_set import magic_set


class TestMagicSet(unittest.TestCase):
    def test_iter(self):
        s = magic_set()
        s.add(1)
        s.add(2)
        s.add(3)

        self.assertEqual(next(s), 1)
        self.assertEqual(next(s), 2)
        self.assertEqual(next(s), 3)


if __name__ == "__main__":
    unittest.main()
