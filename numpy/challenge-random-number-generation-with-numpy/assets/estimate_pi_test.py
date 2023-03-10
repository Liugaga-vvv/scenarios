import sys


sys.path.append("/home/labex/project")

import unittest
from estimate_pi import estimate_pi

class TestEstimatePi(unittest.TestCase):

    def test_estimate_pi(self):
        pi_estimate = estimate_pi(1000000)
        self.assertAlmostEqual(pi_estimate, 3.14159, places=3)

if __name__ == '__main__':
    unittest.main()