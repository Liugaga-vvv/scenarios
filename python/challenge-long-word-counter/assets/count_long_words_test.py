import sys

sys.path.append("/home/labex/project")
import unittest
from count_long_words import count_long_words


class TestCountLongWords(unittest.TestCase):
    def test_count_long_words(self):
        text = "The quick brown fox jumps over the lazy dog"
        self.assertEqual(count_long_words(text, 4), 3)

        text = "A cat in the hat"
        self.assertEqual(count_long_words(text, 3), 0)

        text = "Python is a great language for data science"
        self.assertEqual(count_long_words(text, 5), 3)


if __name__ == "__main__":
    unittest.main()
