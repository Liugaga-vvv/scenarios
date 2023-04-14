import sys

sys.path.append("/home/labex/project/")

import unittest
from magic_set import magic_set


class TestMagicSet(unittest.TestCase):
    def test_eq_ne(self):
        s1 = magic_set()
        s1.add(1)
        s1.add(2)
        s1.add(3)

        s2 = magic_set()
        s2.add(3)
        s2.add(2)
        s2.add(1)

        s3 = magic_set()
        s3.add(1)
        s3.add(2)

        self.assertFalse(s1 != s2)
        self.assertTrue(s1 != s3)


if __name__ == "__main__":
    unittest.main()
