import sys

sys.path.append("/home/labex/project")

import unittest
from solitaire import solitaire


class TestSolitaire(unittest.TestCase):
    def test_solitaire(self):
        result = solitaire([])
        self.assertEqual([], result)

        result = solitaire(['a', 'apple'])
        self.assertEqual(1, len(result))
        self.assertEqual(['a', 'apple'], result[0])

        result = solitaire(['a', 'apple', 'orange'])
        self.assertEqual(2, len(result))
        self.assertEqual(['a', 'apple'], result[0])
        self.assertEqual(['orange'], result[1])


if __name__ == "__main__":
    unittest.main()
