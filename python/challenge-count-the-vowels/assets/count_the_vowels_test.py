import unittest
import sys

sys.path.append("/home/labex/project")

from count_vowels import count_vowels


class TestCountVowels(unittest.TestCase):
    def test_count_vowels(self):
        self.assertEqual(count_vowels("hello"), 2)
        self.assertEqual(count_vowels("world"), 1)
        self.assertEqual(count_vowels("engineering"), 5)
        self.assertEqual(count_vowels("aio"), 3)
        self.assertEqual(count_vowels("vwxyz"), 0)


if __name__ == "__main__":
    unittest.main()
