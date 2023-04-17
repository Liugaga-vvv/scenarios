import sys

sys.path.append("/home/labex/project")
import unittest
import numpy as np
from determinant_matrix import determinant_matrix


class TestDeterminantMatrix(unittest.TestCase):
    def test_determinant_matrix(self):
        A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        B = np.array([[1, 2], [3, 4]])
        self.assertEqual(determinant_matrix(A), 0.0)
        self.assertEqual(determinant_matrix(B), -2.0000000000000004)


if __name__ == "__main__":
    unittest.main()
