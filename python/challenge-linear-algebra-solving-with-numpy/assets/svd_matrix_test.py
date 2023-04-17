import sys

sys.path.append("/home/labex/project")
import unittest
import numpy as np
from svd_matrix import svd_matrix


class TestSingularValueDecomposition(unittest.TestCase):
    def test_svd_matrix(self):
        A = np.array([[2, 3, 4], [4, 8, 10], [7, 8, 9]])
        U, S, V = svd_matrix(A)
        self.assertTrue(np.allclose(U @ np.diag(S) @ V, A))


if __name__ == "__main__":
    unittest.main()
