def validate_user_input(self, num1, num2, operation):
    """
    Validate the user input to make sure it is correct. If the input is invalid, print an error message.

    Args:
        num1(str): The first entered number.
        num2(str): The second entered number.
        operation(str): The entered operation.

    Returns:
        error_message(str): The error message when the input is invalid.
    """
    error_message = None
    if not (num1.isdigit() and num2.isdigit()):
        error_message = "Please enter valid numbers"
    elif operation not in ["+", "-", "*", "/"]:
        error_message = "Please enter a valid operation"
    print(error_message)
    return error_message
