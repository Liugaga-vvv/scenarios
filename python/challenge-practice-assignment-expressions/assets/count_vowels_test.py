import sys

sys.path.append("/home/labex/project/")

import unittest
from count_vowels import count_vowels


class TestAssignmentExpressionsChallenge(unittest.TestCase):
    def test_count_vowels(self):
        test_cases = [
            ("The quick brown fox jumps over the lazy dog", 11),
            ("Aeiou", 5),
            ("AEIOU", 5),
            ("bcdfgh", 0),
            ("", 0),
        ]

        for s, expected in test_cases:
            self.assertEqual(count_vowels(s), expected)


if __name__ == "__main__":
    unittest.main()
