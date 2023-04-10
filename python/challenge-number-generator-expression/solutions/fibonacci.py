def fibonacci(n: int) -> Generator[int, None, None]:
    """
    Returns a generator that yields the first n Fibonacci numbers.

    Args:
    n: The number of Fibonacci numbers to generate.

    Yields:
    The first n Fibonacci numbers.
    """
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
