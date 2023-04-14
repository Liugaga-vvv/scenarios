import math
import os
import unittest
import sys

sys.path.append("/home/labex/project")

from number import MyNumber


class TestFileSearch(unittest.TestCase):
    def test_file_search(self):

        with open("/home/labex/project/number.py", "r") as f:
            contents = f.read()
            for string in ["__neg__", "__abs__", "__round__", "__floor__", "__ceil__"]:
                self.assertIn(string, contents)

    def test_mynumber(self):
        a = MyNumber(5.678)
        a.value
        -a.value
        abs(a).value
        round(a, 2).value
        math.floor(a).value
        math.ceil(a).value

    def test_complete_example(self):
        with open("/home/labex/project/unary_example.py", "r") as f:
            contents = f.read()
            for string in ["MyNumber", "-", "abs", "round", "floor", "ceil"]:
                self.assertIn(string, contents)

    def test_run_example(self):
        output = os.popen('cat ~/.zsh_history | grep "unary_example.py"').read()
        self.assertNotEqual("", output)


if __name__ == "__main__":
    unittest.main()
