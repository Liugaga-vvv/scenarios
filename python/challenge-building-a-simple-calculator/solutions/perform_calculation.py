def perform_calculation(self, num1, num2, operation):
    """
    Once the user input has been validated, perform the calculation and return the result.

    Args:
        num1(str): The first entered number.
        num2(str): The second entered number.
        operation(str): The entered operation.

    Returns:
        result(float): The result of the calculation.
    """
    num1 = float(num1)
    num2 = float(num2)
    result = None
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    else:
        result = num1 / num2
    return result
