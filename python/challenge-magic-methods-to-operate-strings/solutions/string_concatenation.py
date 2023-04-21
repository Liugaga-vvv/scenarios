class MyString:
    def __init__(self, string: str):
        self.string = string

    def __add__(self, other: "MyString") -> "MyString":
        """Concatenate two MyString objects.

        Args:
            other (MyString): The other MyString object to concatenate with.

        Returns:
            MyString: A new MyString object with the concatenated string.
        """
        return MyString(self.string + other.string)
