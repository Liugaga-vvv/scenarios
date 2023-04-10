import sys

sys.path.append("/home/labex/project/")

import unittest
from magic_set import magic_set


class TestMagicSet(unittest.TestCase):
    def test_init(self):
        s = magic_set()
        s.add(1)
        s.add(2)
        s.add(3)
        s.clear()
        print(s._data)
        self.assertEqual(s._data, [])


if __name__ == "__main__":
    unittest.main()
