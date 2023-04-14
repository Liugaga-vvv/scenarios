class MathExpression:
    def __init__(self, value: int):
        self.value = value

    def __add__(self, other: "MathExpression") -> "MathExpression":
        """Adds two instances of the class together.

        Args:
            other (MathExpression): The other MathExpression object to add

        Returns:
            MathExpression: A new MathExpression object containing the computed result
        """
        return MathExpression(self.value + other.value)

    def __sub__(self, other: "MathExpression") -> "MathExpression":
        """Subtracts one instance of the class from another.

        Args:
            other (MathExpression): The other MathExpression object to sub

        Returns:
            MathExpression: A new MathExpression object containing the computed result
        """
        return MathExpression(self.value - other.value)

    def __mul__(self, other: "MathExpression") -> "MathExpression":
        """Multiplies two instances of the class together.

        Args:
            other (MathExpression): The other MathExpression object to mul

        Returns:
            MathExpression: A new MathExpression object containing the computed result
        """
        return MathExpression(self.value * other.value)

    def __truediv__(self, other: "MathExpression") -> "MathExpression":
        """Divides one instance of the class by another.

        Args:
            other (MathExpression): The other MathExpression object to truediv

        Returns:
            MathExpression:A new MathExpression object containing the computed result
        """
        return MathExpression(self.value / other.value)

    def __str__(self) -> str:
        """Returns a string representation of the value of the instance.

        Returns:
            str: Stringify the object
        """
        return str(self.value)
