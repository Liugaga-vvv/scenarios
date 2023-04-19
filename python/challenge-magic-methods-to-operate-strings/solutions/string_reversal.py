class MyString:
    def __init__(self, string: str):
        self.string = string

    def __reversed__(self) -> str:
        """Return a reversed version of the string.

        Returns:
            str: The reversed string.
        """
        return self.string[::-1]
