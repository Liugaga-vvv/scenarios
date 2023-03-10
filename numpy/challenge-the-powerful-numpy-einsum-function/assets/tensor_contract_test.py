import sys


sys.path.append("/home/labex/project")

import unittest
import numpy as np
from tensor_contract import tensor_contract
from unittest.mock import patch

class TestTensorContraction(unittest.TestCase):
    @patch('numpy.einsum')
    def test_tensor_contract(self, mock_einsum):
        A = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]])
        B = np.array([[13, 14], [15, 16]])
        tensor_contract(A,B)
        mock_einsum.assert_called_once_with('ijk, kl -> ijl', A, B)

if __name__ == '__main__':
    unittest.main()