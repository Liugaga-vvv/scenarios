def get_user_input(self):
    """
    Return the entered two numbers and an operation.

    Args:
        None

    Returns:
        tuple: num1, num2, operation
    """
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    operation = input("Enter an operation (+, -, *, or /): ")
    return num1, num2, operation
