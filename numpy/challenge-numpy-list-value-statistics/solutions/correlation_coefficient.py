import numpy as np
from typing import List


def correlation_coefficient(x: List[float], y: List[float]) -> float:
    """
    Computes the correlation coefficient between two lists of numbers using NumPy.

    Args:
        x: A list of numbers.
        y: A list of numbers.

    Returns:
        The correlation coefficient between x and y.
    """
    corrcoef_matrix = np.corrcoef(x, y)
    corrcoef = corrcoef_matrix[0, 1]
    return corrcoef
