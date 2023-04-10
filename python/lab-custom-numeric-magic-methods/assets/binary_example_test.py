import os
import unittest
import sys

sys.path.append("/home/labex/project")

from number import MyNumber


class TestFileSearch(unittest.TestCase):
    def test_file_search(self):

        with open("/home/labex/project/number.py", "r") as f:
            contents = f.read()
            for string in [
                "__add__",
                "__sub__",
                "__mul__",
                "__truediv__",
                "__floordiv__",
                "__mod__",
                "__pow__",
            ]:
                self.assertIn(string, contents)

    def test_mynumber(self):
        a = MyNumber(5)
        b = MyNumber(3)
        a + b
        a - b
        a * b
        a / b
        a // b
        a % b
        a**b

    def test_complete_example(self):
        with open("/home/labex/project/binary_example.py", "r") as f:
            contents = f.read()
            for string in ["+", "-", "*", "/", "//", "%", "**"]:
                self.assertIn(string, contents)

    def test_run_example(self):
        output = os.popen('cat ~/.zsh_history | grep "binary_example.py"').read()
        self.assertNotEqual("", output)


if __name__ == "__main__":
    unittest.main()
