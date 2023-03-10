import sys


sys.path.append("/home/labex/project")

import unittest
import numpy as np
from matmul import matmul
from unittest.mock import patch

class TestMatrixMultiplication(unittest.TestCase):
    @patch('numpy.einsum')
    def test_matmul(self, mock_einsum):
        A = np.array([[1, 2], [3, 4], [5, 6]])
        B = np.array([[7, 8], [9, 10]])
        matmul(A, B)
        mock_einsum.assert_called_once_with('ij, jk -> ik', A, B)

if __name__ == '__main__':
    unittest.main()