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

        for i, item in enumerate(s):
            self.assertEqual(item, i + 1)


if __name__ == "__main__":
    unittest.main()
