class MathExpression:
    def __init__(self, value: int):
        self.value = value

    def __iadd__(self, other: "MathExpression") -> "MathExpression":
        """Adds another instance of the class to the current instance.

        Args:
            other (MathExpression): The other MathExpression object to iadd

        Returns:
            MathExpression: A new MathExpression object containing the computed result
        """
        self.value += other.value
        return self

    def __isub__(self, other: "MathExpression") -> "MathExpression":
        """Subtracts another instance of the class from the current instance.

        Args:
            other (MathExpression): The other MathExpression object to isub

        Returns:
            MathExpression: A new MathExpression object containing the computed result
        """
        self.value -= other.value
        return self

    def __imul__(self, other: "MathExpression") -> "MathExpression":
        """Multiplies another instance of the class with the current instance.

        Args:
            other (MathExpression): The other MathExpression object to imul

        Returns:
            MathExpression: A new MathExpression object containing the computed result
        """
        self.value *= other.value
        return self

    def __itruediv__(self, other: "MathExpression") -> "MathExpression":
        """Divides the current instance by another instance of the class.

        Args:
            other (MathExpression): The other MathExpression object to itruediv

        Returns:
            MathExpression: A new MathExpression object containing the computed result
        """
        self.value /= other.value
        return self

    def __str__(self) -> str:
        """Returns a string representation of the value of the instance.

        Returns:
            str: Stringify the object
        """
        return str(self.value)
