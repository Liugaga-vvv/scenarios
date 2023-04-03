from typing import List
from multiprocessing import Pool

def square_multiprocessing(integers: List[int]) -> List[int]:
    """
    Calculate the square of each integer in the input list using multiprocessing.

    Args:
        integers: A list of non-negative integers.

    Returns:
        A list of integers, where each element is the square of the corresponding
        element in the input list.

    """
    with Pool() as pool:
        results = pool.map(square, integers)
    return results

def square(x: int) -> int:
    """
    Calculate the square of an integer.

    Args:
        x: A non-negative integer.

    Returns:
        The square of the input integer.

    """
    return x*x
