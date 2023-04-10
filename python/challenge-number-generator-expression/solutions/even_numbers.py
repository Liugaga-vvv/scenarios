from ast import List
from typing import Generator


def even_numbers(numbers: List[int]) -> Generator[int, None, None]:
    """
    Returns a generator that yields only even numbers from the input list.

    Args:
    numbers: A list of integers.

    Yields:
    The even numbers from the input list.
    """
    return (number for number in numbers if number % 2 == 0)
