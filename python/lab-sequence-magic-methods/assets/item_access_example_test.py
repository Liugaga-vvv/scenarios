import os
import unittest
import sys

sys.path.append("/home/labex/project")

from sequence import MySequence


class TestFileSearch(unittest.TestCase):
    def test_file_search(self):

        with open("/home/labex/project/sequence.py", "r") as f:
            contents = f.read()
            for string in ["__getitem__", "__setitem__", "__delitem__"]:
                self.assertIn(string, contents)

    def test_mysequence(self):
        my_seq = MySequence([1, 2, 3, 4, 5])
        my_seq[2]
        my_seq[2] = 9
        del my_seq[2]

    def test_complete_example(self):
        with open("/home/labex/project/item_access_example.py", "r") as f:
            contents = f.read()
            for string in ["[", "]", "=", "del"]:
                self.assertIn(string, contents)

    def test_run_example(self):
        output = os.popen('cat ~/.zsh_history | grep "item_access_example.py"').read()
        self.assertNotEqual("", output)


if __name__ == "__main__":
    unittest.main()
