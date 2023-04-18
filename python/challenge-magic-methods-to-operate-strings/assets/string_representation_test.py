import sys

sys.path.append("/home/labex/project")

from string_representation import MyString

import unittest


class TestMyString(unittest.TestCase):
    def test_repr(self):
        s1 = MyString("Hello")
        s2 = repr(s1)
        self.assertEqual(s2, "MyString('Hello')")


if __name__ == "__main__":
    unittest.main()
