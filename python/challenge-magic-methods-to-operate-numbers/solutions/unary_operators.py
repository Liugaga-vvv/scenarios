class MathExpression:
    def __init__(self, value: int):
        self.value = value

    def __neg__(self) -> "MathExpression":
        """Returns the negation of the instance of the class.

        Returns:
            MathExpression: A new MathExpression object containing the result converted to a negative number.
        """
        return MathExpression(-self.value)

    def __pos__(self) -> "MathExpression":
        """Returns the positive value of the instance of the class.

        Returns:
            MathExpression: A new MathExpression object containing the result converted to a positive number.
        """
        return MathExpression(abs(self.value))

    def __abs__(self) -> "MathExpression":
        """Returns the absolute value of the instance of the class.

        Returns:
            MathExpression: A new MathExpression object containing the results converted to absolute values.
        """
        return MathExpression(abs(self.value))

    def __str__(self) -> str:
        """Returns a string representation of the value of the instance.

        Returns:
            str: Stringify the object
        """
        return str(self.value)
