class simple_calculator:
    """
    This function prompts the user to enter two numbers and an operation (+, -, *, or /),
    validates the user input to make sure it is correct,
    performs the appropriate calculation based on the operation entered,
    and displays the result to the user.
    """

    def get_user_input(self):
        """
        Return the entered two numbers and an operation.

        Args:
            None

        Returns:
            tuple: num1, num2, operation
        """
        num1 = None
        num2 = None
        operation = None
        return num1, num2, operation

    def validate_user_input(self, num1: str, num2: str, operation: str) -> str:
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
        if not (None and None):
            error_message = "Please enter valid numbers"
            print(error_message)
        elif None:
            error_message = "Please enter a valid operation"
            print(error_message)
        return error_message

    def perform_calculation(self, num1: str, num2: str, operation: str) -> float:
        """
        Once the user input has been validated, perform the calculation and return the result.

        Args:
            num1(str): The first entered number.
            num2(str): The second entered number.
            operation(str): The entered operation.

        Returns:
            result(float): The result of the calculation.
        """
        num1 = None
        num2 = None
        result = None
        if operation == "+":
            result = None
        elif operation == "-":
            result = None
        elif operation == "*":
            result = None
        else:
            result = None
        return result

    def display_result(self, result: float) -> str:
        """
        Display the result of the calculation to the user.

        Args:
            result(float): The result of the calculation.

        Returns:
            output(str): Display the result of the calculation
        """
        output = "Result: " + None
        print(output)
        return output
