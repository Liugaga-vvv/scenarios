from ast import List
from typing import Generator


def square_numbers(numbers: List[int]) -> Generator[int, None, None]:
    """
    Returns a generator that yields the square of each number in the input list.

    Args:
    numbers: A list of integers.

    Yields:
    The square of each integer in the input list.
    """
    return (number**2 for number in numbers)
