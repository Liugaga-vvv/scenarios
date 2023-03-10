import sys


sys.path.append("/home/labex/project")

import unittest
import numpy as np
from sample_multinomial import sample_multinomial

class TestSampleMultinomial(unittest.TestCase):

    def test_sample_multinomial(self):
        probs = np.array([0.2, 0.3, 0.5])
        n = 10
        result = sample_multinomial(probs, n)
        self.assertIsInstance(result, np.ndarray)
        self.assertEqual(result.size, probs.size)
        self.assertEqual(np.sum(result), n)

if __name__ == '__main__':
    unittest.main()