import numpy as np
from invert_matrix import invert_matrix


def solve_linear_equation(A: np.ndarray, b: np.ndarray) -> np.ndarray:
    """
    Solves the linear equation Ax = b using matrix inversion.
    If the matrix A is not invertible or the dimensions of A and b do not match,
    raises a ValueError with an appropriate error message.

    Args:
        A: A NumPy matrix representing the coefficients of the linear equation.
        b: A NumPy matrix representing the constants of the linear equation.

    Returns:
        The solution to the linear equation Ax = b as a NumPy array.

    Raises:
        ValueError: If the matrix A is not invertible or the dimensions of A and b do not match.
    """
    if A.shape[0] != A.shape[1] or A.shape[0] != b.shape[0]:
        raise ValueError("Matrix A and matrix b dimensions do not match")
    inv_A = invert_matrix(A)
    return np.matmul(inv_A, b)
