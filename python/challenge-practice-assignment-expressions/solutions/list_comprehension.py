from typing import List


def list_comprehension() -> List:
    """
    Generate a list of squares of even numbers between 1 and 10 using the walrus operator.

    Returns:
        List[int]: List of squares of even numbers between 1 and 10.
    """

    squares = [square for x in range(1, 11) if (square := x * x) % 2 == 0]
    return squares
