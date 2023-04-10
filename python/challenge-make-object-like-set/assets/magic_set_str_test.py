import sys

sys.path.append("/home/labex/project/")

import unittest
from magic_set import magic_set


class TestMagicSet(unittest.TestCase):
    def test_str(self):
        s = magic_set()
        self.assertEqual(str(s), "set()")

        s.add(1)
        s.add(2)
        s.add(3)
        self.assertEqual(str(s), "{1, 2, 3}")


if __name__ == "__main__":
    unittest.main()
