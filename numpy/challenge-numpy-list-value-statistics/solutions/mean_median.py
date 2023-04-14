import numpy as np
from typing import List, Tuple


def mean_median(numbers: List[float]) -> Tuple[float, float]:
    """
    Computes the mean and median of a list of numbers using NumPy.

    Args:
        numbers: A list of numbers.

    Returns:
        A tuple containing the mean and median.
    """
    mean = np.mean(numbers)
    median = np.median(numbers)

    return mean, median
