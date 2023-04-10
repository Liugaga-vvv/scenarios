from typing import Generator


def factorial(n: int) -> Generator[int, None, None]:
    """
    Returns a generator that yields the factorial of n.

    Args:
    n: The number to compute the factorial of.

    Yields:
    The factorial of n.
    """
    result = 1
    for i in range(1, n + 1):
        result *= i
        yield result
