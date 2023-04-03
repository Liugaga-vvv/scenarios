from unittest.mock import patch
from estimate_pi import estimate_pi
import unittest
import sys


sys.path.append("/home/labex/project")


class TestEstimatePi(unittest.TestCase):

    def test_estimate_pi(self):
        pi_estimate = estimate_pi(1000000)
        self.assertAlmostEqual(pi_estimate, 3.14159, places=2)

    @patch('numpy.random.rand')
    def test_called(self, mock_random):
        pi_estimate = estimate_pi(1000000)
        mock_random.assert_called_with(pi_estimate)


if __name__ == '__main__':
    unittest.main()
