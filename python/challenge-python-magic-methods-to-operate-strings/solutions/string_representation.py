class MyString:
    def __init__(self, string: str):
        self.string = string

    def __repr__(self) -> str:
        """Return a string representation of the object.

        Returns:
            str: The string representation of the object.
        """
        return f"MyString('{self.string}')"
