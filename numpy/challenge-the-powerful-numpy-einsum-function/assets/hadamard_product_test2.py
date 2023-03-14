import sys


sys.path.append("/home/labex/project")

import unittest
import numpy as np
from hadamard_product import hadamard_product

class TestHadamardProduct(unittest.TestCase):
    def test_hadamard_product(self):
        A = np.array([[1, 2], [3, 4], [5, 6]])
        B = np.array([[7, 8], [9, 10], [11, 12]])
        expected_result = np.array([[7, 16], [27, 40], [55, 72]])
        self.assertTrue(np.allclose(hadamard_product(A, B), expected_result))

if __name__ == '__main__':
    unittest.main()