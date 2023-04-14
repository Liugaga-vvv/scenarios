import sys

sys.path.append("/home/labex/project")

from string_concatenation import MyString

import unittest


class TestMyString(unittest.TestCase):
    def test_add(self):
        s1 = MyString("Hello")
        s2 = MyString("World")
        s3 = s1 + s2
        self.assertEqual(s3, "HelloWorld")


if __name__ == "__main__":
    unittest.main()
