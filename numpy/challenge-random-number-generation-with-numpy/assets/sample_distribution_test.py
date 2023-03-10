import sys


sys.path.append("/home/labex/project")

import unittest
import numpy as np
from sample_distribution import sample_distribution

class TestSampleDistribution(unittest.TestCase):

    def test_sample_distribution(self):
        probs = np.array([0.1, 0.2, 0.3, 0.4])
        result = sample_distribution(probs)
        self.assertTrue(0 <= result < probs.size)

if __name__ == '__main__':
    unittest.main()