import sys


sys.path.append("/home/labex/project")

import unittest
import numpy as np
from trace_of_matrix import trace
from unittest.mock import patch


class TestTrace(unittest.TestCase):
    @patch('numpy.einsum')
    def test_trace(self, mock_einsum):
        A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        trace(A)
        mock_einsum.assert_called_once_with('ii', A)

if __name__ == '__main__':
    unittest.main()