import sys

sys.path.append("/home/labex/project")

import unittest
from split_sentence import split_sentence


class TestSplitSentence(unittest.TestCase):
    def test_split_sentence(self):
        sentence = ""
        result = split_sentence(sentence)
        self.assertTrue(not result)
        self.assertEqual([], result)

        sentence = "Some red apples in a red basket"
        result = split_sentence(sentence)
        self.assertTrue(result)
        self.assertEqual(6, len(result))
        self.assertTrue('some' in result)

if __name__ == "__main__":
    unittest.main()
