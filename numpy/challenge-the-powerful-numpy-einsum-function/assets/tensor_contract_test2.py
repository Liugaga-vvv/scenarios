import sys


sys.path.append("/home/labex/project")

import unittest
import numpy as np
from tensor_contract import tensor_contract

class TestTensorContraction(unittest.TestCase):
    def test_tensor_contract(self):
        A = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]])
        B = np.array([[13, 14], [15, 16]])
        expected_result = np.array([[[43, 46], [99, 106]], [[155, 166], [211, 226]], [[267, 286], [323, 346]]])
        self.assertTrue(np.allclose(tensor_contract(A, B), expected_result))

if __name__ == '__main__':
    unittest.main()