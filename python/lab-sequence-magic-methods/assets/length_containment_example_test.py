import os
import unittest
import sys

sys.path.append("/home/labex/project")

from sequence import MySequence


class TestFileSearch(unittest.TestCase):
    def test_file_search(self):

        with open("/home/labex/project/sequence.py", "r") as f:
            contents = f.read()
            for string in ["__init__", "__len__", "__contains__"]:
                self.assertIn(string, contents)

    def test_mysequence(self):
        my_seq = MySequence([1, 2, 3, 4, 5])
        len(my_seq)
        3 in my_seq

    def test_complete_example(self):
        with open("/home/labex/project/length_containment_example.py", "r") as f:
            contents = f.read()
            for string in ["len", "not in"]:
                self.assertIn(string, contents)

    def test_run_example(self):
        output = os.popen(
            'cat ~/.zsh_history | grep "length_containment_example.py"'
        ).read()
        self.assertNotEqual("", output)


if __name__ == "__main__":
    unittest.main()
