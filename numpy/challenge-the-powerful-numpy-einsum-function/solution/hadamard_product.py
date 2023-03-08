import numpy as np

def hadamard_product(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    """
    Compute the Hadamard product of two matrices using NumPy's einsum function.

    Parameters:
    -----------
    A : numpy.ndarray
        Input matrix A of shape (M, N).
    B : numpy.ndarray
        Input matrix B of shape (M, N).

    Returns:
    --------
    numpy.ndarray
        Resulting matrix of shape (M, N).
    """
    return np.einsum('ij, ij -> ij', A, B)