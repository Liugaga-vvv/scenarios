import numpy as np

def matmul(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    """
    Matrix multiplication using NumPy's einsum function.

    Parameters:
    -----------
    A : numpy.ndarray
        Input matrix A of shape (M, N).
    B : numpy.ndarray
        Input matrix B of shape (N, K).

    Returns:
    --------
    numpy.ndarray
        Resulting matrix of shape (M, K).
    """
    return np.einsum('ij, jk -> ik', A, B)
