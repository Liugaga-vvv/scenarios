class MathExpression:
    def __init__(self, value: int):
        """Initializes the class with an integer value.

        Args:
            value (int): An integer used to initialize the class
        """
        self.value = None

    def __add__(self, other: "MathExpression") -> "MathExpression":
        """Adds two instances of the class together.

        Args:
            other (MathExpression): The other MathExpression object to add

        Returns:
            MathExpression: A new MathExpression object containing the computed result
        """

        # TODO

        return

    def __sub__(self, other: "MathExpression") -> "MathExpression":
        """Subtracts one instance of the class from another.

        Args:
            other (MathExpression): The other MathExpression object to sub

        Returns:
            MathExpression: A new MathExpression object containing the computed result
        """

        # TODO

        return

    def __mul__(self, other: "MathExpression") -> "MathExpression":
        """Multiplies two instances of the class together.

        Args:
            other (MathExpression): The other MathExpression object to mul

        Returns:
            MathExpression: A new MathExpression object containing the computed result
        """

        # TODO

        return

    def __truediv__(self, other: "MathExpression") -> "MathExpression":
        """Divides one instance of the class by another.

        Args:
            other (MathExpression): The other MathExpression object to truediv

        Returns:
            MathExpression:A new MathExpression object containing the computed result
        """

        # TODO

        return

    def __str__(self) -> str:
        """Returns a string representation of the value of the instance.

        Returns:
            str: Stringify the object
        """
        return str()
