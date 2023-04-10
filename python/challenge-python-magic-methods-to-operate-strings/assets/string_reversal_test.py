import sys

sys.path.append("/home/labex/project")

from string_reversal import MyString

import unittest


class TestMyString(unittest.TestCase):
    def test_reversed(self):
        s1 = MyString("Hello")
        s2 = reversed(s1)
        self.assertEqual(s2, "olleH")


if __name__ == "__main__":
    unittest.main()
