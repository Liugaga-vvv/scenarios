import sys

sys.path.append("/home/labex/project")
import unittest
import numpy as np
from eigenvector_eigenvalue import eigenvector_eigenvalue


class TestEigenvectorEigenvalueCalculation(unittest.TestCase):
    def test_eigenvector_eigenvalue(self):
        A = np.array([[2, 2], [2, 4]])
        eigvals, eigvecs = eigenvector_eigenvalue(A)
        self.assertTrue(
            np.allclose(eigvecs @ np.diag(eigvals) @ np.linalg.inv(eigvecs), A)
        )


if __name__ == "__main__":
    unittest.main()
