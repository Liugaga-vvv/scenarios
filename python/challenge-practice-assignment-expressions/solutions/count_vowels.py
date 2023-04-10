def count_vowels(s: str) -> int:
    """
    Count the number of vowels in the given string using the walrus operator.

    Args:
        s (str): The input string.

    Returns:
        int: The number of vowels in the input string.
    """
    return sum((count := c.lower() in "aeiou") for c in s)
