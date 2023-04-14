import sys


sys.path.append("/home/labex/project")

import unittest
import numpy as np
from hadamard_product import hadamard_product
from unittest.mock import patch

class TestHadamardProduct(unittest.TestCase):
    @patch('numpy.einsum')
    def test_hadamard_product(self, mock_einsum):
        A = np.array([[1, 2], [3, 4], [5, 6]])
        B = np.array([[7, 8], [9, 10], [11, 12]])
        hadamard_product(A,B)
        mock_einsum.assert_called_once_with('ij, ij -> ij', A, B)

if __name__ == '__main__':
    unittest.main()