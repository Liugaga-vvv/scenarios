import sys

sys.path.append("/home/labex/project")

from string_comparison import MyString

import unittest


class TestMyString(unittest.TestCase):
    def test_eq(self):
        s1 = MyString("abc")
        s2 = MyString("abc")
        self.assertEqual(s1, s2)

    def test_ne(self):
        s1 = MyString("abc")
        s2 = MyString("def")
        self.assertNotEqual(s1, s2)

    def test_lt(self):
        s1 = MyString("abc")
        s2 = MyString("def")
        self.assertLess(s1, s2)

    def test_le(self):
        s1 = MyString("abc")
        s2 = MyString("abc")
        self.assertLessEqual(s1, s2)

    def test_gt(self):
        s1 = MyString("def")
        s2 = MyString("abc")
        self.assertGreater(s1, s2)

    def test_ge(self):
        s1 = MyString("abc")
        s2 = MyString("abc")
        self.assertGreaterEqual(s1, s2)


if __name__ == "__main__":
    unittest.main()
