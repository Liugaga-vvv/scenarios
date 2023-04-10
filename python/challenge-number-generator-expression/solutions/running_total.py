from ast import List
from typing import Generator


def running_total(numbers: List[int]) -> Generator[int, None, None]:
    """
    Returns a generator that yields the running total of the numbers in the input list.

    Args:
    numbers: A list of integers.

    Yields:
    The running total of the numbers in the input list.
    """
    total = 0
    for number in numbers:
        total += number
        yield total
