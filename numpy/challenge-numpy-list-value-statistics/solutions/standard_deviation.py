import numpy as np
from typing import List


def standard_deviation(numbers: List[float]) -> float:
    """
    Computes the standard deviation of a list of numbers using NumPy.

    Args:
        numbers: A list of numbers.

    Returns:
        The standard deviation of the list of numbers.
    """
    standard = np.std(numbers)
    return standard
