import sys


sys.path.append("/home/labex/project")

import unittest
import numpy as np
from shuffle_deck import shuffle_deck

class TestShuffleDeck(unittest.TestCase):

    def test_shuffle_deck(self):
        result = shuffle_deck()
        self.assertIsInstance(result, np.ndarray)
        self.assertEqual(result.size, 52)
        self.assertTrue(np.all(np.unique(result) == np.arange(1, 53)))

if __name__ == '__main__':
    unittest.main()