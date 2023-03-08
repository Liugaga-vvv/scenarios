import sys


sys.path.append("/home/labex/project")

import unittest
import numpy as np
from matmul import matmul

class TestMatrixMultiplication(unittest.TestCase):

    def test_matmul(self):
        A = np.array([[1, 2], [3, 4], [5, 6]])
        B = np.array([[7, 8], [9, 10]])
        expected_result = np.array([[25, 28], [57, 64], [89, 100]])
        self.assertTrue(np.allclose(matmul(A, B), expected_result))

if __name__ == '__main__':
    unittest.main()