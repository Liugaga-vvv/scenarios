import numpy as np


def matrix_multiply(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """
    Multiplies two numpy arrays as matrices and returns the result.

    Parameters:
    a (numpy.ndarray): The first input array.
    b (numpy.ndarray): The second input array.

    Returns:
    numpy.ndarray: The matrix product of the two input arrays.
    """
    return np.matmul(a, b)
