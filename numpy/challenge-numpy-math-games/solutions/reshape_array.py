import numpy as np


def reshape_array(a: np.ndarray, shape: tuple[int]) -> np.ndarray:
    """
    Reshapes a numpy array to the specified shape and returns the result.

    Parameters:
    a (numpy.ndarray): The input array to be reshaped.
    shape (Tuple[int]): The desired shape of the output array.

    Returns:
    numpy.ndarray: The reshaped array.
    """
    return np.reshape(a, shape)
