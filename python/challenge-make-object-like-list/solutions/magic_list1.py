from typing import List, Union


class MagicList:
    """
    A class that behaves like a list, but with magic methods that make it even more powerful.
    """

    def __init__(self, *args) -> None:
        """
        Initializes the list with the given values.

        Args:
            *args: Any number of values to initialize the list.
        """
        self._data = list(args)

    def __len__(self) -> int:
        """
        Returns the length of the list.

        Returns:
            int: The length of the list.
        """
        length = len(self._data)
        return length

    def __str__(self) -> str:
        """
        Returns a string representation of the list.

        Returns:
            str: A string representation of the list.
        """
        string_list = str(self._data)
        return string_list

    def __contains__(self, item: any) -> bool:
        """
        Returns True if the given item is in the list.

        Args:
            item (any): The item to search for.

        Returns:
            bool: True if the item is in the list, False otherwise.
        """
        isInlist = item in self._data
        return isInlist
