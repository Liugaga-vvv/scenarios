import os
import unittest
import sys

sys.path.append("/home/labex/project")

from number import MyNumber


class TestFileSearch(unittest.TestCase):
    def test_run_example1(self):
        output = os.popen('cat ~/.zsh_history | grep "inplace_example1.py"').read()
        self.assertIsNotNone(output)

    def test_file_search(self):

        with open("/home/labex/project/number.py", "r") as f:
            contents = f.read()
            for string in [
                "__iadd__",
                "__isub__",
                "__imul__",
                "__itruediv__",
                "__ifloordiv__",
                "__imod__",
                "__ipow__",
            ]:
                self.assertIn(string, contents)

    def test_mynumber(self):
        a = MyNumber(5)
        b = MyNumber(3)
        a += b
        a -= b
        a *= b
        a /= b
        a //= b
        a %= b
        a **= b

    def test_complete_example(self):
        with open("/home/labex/project/inplace_example2.py", "r") as f:
            contents = f.read()
            for string in ["+=", "-=", "*=", "/=", "//=", "%=", "**="]:
                self.assertIn(string, contents)

    def test_run_example2(self):
        output = os.popen('cat ~/.zsh_history | grep "inplace_example2.py"').read()
        self.assertNotEqual("", output)


if __name__ == "__main__":
    unittest.main()
