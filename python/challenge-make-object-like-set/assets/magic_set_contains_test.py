import sys

sys.path.append("/home/labex/project")

import unittest
from magic_set import magic_set


class TestMagicSet(unittest.TestCase):
    def test_contains(self):
        s = magic_set()
        s.add(1)
        s.add(2)
        s.add(3)

        self.assertTrue(1 in s)
        self.assertTrue(2 in s)
        self.assertTrue(3 in s)
        self.assertFalse(4 in s)


if __name__ == "__main__":
    unittest.main()
