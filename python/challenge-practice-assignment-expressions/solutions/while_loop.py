def while_loop() -> int:
    """
    Read integers from the user until they enter 0. Calculate and return the sum of all entered numbers using the walrus operator.

    Returns:
        int: The sum of the entered numbers.
    """

    total = 0
    while (number := int(input("Enter a number (0 to stop): "))) != 0:
        total += number

    return total
