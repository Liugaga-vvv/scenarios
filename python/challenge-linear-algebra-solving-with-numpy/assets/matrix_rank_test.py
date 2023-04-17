import sys

sys.path.append("/home/labex/project")
import unittest
import numpy as np
from matrix_rank import matrix_rank


class TestMatrixRank(unittest.TestCase):
    def test_matrix_rank(self):
        A = np.array([[1, 3], [2, 4]])
        B = np.array([[1, 6, 3], [4, 7, 6], [7, 8, 9]])
        C = np.array([[1, 5, 3], [4, 5, 9], [7, 4, 9], [10, 14, 12]])
        self.assertEqual(matrix_rank(A), 2)
        self.assertEqual(matrix_rank(B), 2)
        self.assertEqual(matrix_rank(C), 3)


if __name__ == "__main__":
    unittest.main()
