import numpy as np


def euclidean_distance(a: np.ndarray, b: np.ndarray) -> float:
    """
    Calculates the Euclidean distance between two numpy arrays.

    Args:
    a (np.ndarray): 1D numpy array
    b (np.ndarray): 1D numpy array

    Returns:
    float: Euclidean distance between the two arrays
    """
    return np.sqrt(np.sum((a - b) ** 2))
