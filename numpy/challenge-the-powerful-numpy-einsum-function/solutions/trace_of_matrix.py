import numpy as np

def trace(A: np.ndarray) -> float:
    """
    Compute the trace of a matrix using NumPy's einsum function.

    Parameters:
    -----------
    A : numpy.ndarray
        Input matrix A of shape (N, N).

    Returns:
    --------
    float
        Trace of the input matrix A.
    """
    return np.einsum('ii', A)