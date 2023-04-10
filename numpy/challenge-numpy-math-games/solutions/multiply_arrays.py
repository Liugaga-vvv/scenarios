import numpy as np


def multiply_arrays(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """
    Multiplies two numpy arrays element-wise and returns the result.

    Parameters:
    a (numpy.ndarray): The first input array.
    b (numpy.ndarray): The second input array.

    Returns:
    numpy.ndarray: The element-wise product of the two input arrays.
    """
    return np.multiply(a, b)
