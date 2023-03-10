import sys


sys.path.append("/home/labex/project")

import unittest
import numpy as np
from generate_markov_chain import generate_markov_chain

class TestGenerateMarkovChain(unittest.TestCase):

    def test_generate_markov_chain(self):
        n = 3
        result = generate_markov_chain(n)
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 2)
        self.assertIsInstance(result[0], np.ndarray)
        self.assertEqual(result[0].shape, (n, n))
        self.assertIsInstance(result[1], np.ndarray)
        self.assertEqual(result[1].shape, (n,))
        self.assertAlmostEqual(np.sum(result[1]), 1.0)

if __name__ == '__main__':
    unittest.main()