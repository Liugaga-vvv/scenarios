import sys


sys.path.append("/home/labex/project")

import unittest
import numpy as np
from einsum_convention import einsum_convention
from unittest.mock import patch

class TestEinsteinSummationConvention(unittest.TestCase):
    @patch('numpy.einsum')
    def test_einsum_convention(self, mock_einsum):
        A = np.array([[1, 2], [3, 4], [5, 6]])
        B = np.array([[7, 8], [9, 10]])
        expected_result = np.array([[25, 28], [57, 64], [89, 100]])
        einsum_convention(A,B)
        mock_einsum.assert_called_once_with('ij, jk -> ik', A, B)
      
if __name__ == '__main__':
    unittest.main()