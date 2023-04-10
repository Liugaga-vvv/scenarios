from typing import Any


class DictLikeObject:
    """
    A class that behaves like a dictionary using magic methods.
    """

    def __init__(self):
        self._data = {}

    def __getitem__(self, key: str) -> Any:
        """
        Retrieve the value for a given key using square bracket notation.

        Args:
            key: The key to retrieve the value for.

        Returns:
            The value for the given key.

        Raises:
            KeyError: If the key does not exist in the dictionary.
        """

        return self._data[key]

    def __setitem__(self, key: str, value: Any) -> None:
        """
        Set the value for a given key using square bracket notation.

        Args:
            key: The key to set the value for.
            value: The value to set.

        Returns:
            None.
        """
        self._data[key] = value

    def __delitem__(self, key: str) -> None:
        """
        Remove the key-value pair for a given key using square bracket notation.

        Args:
            key: The key to remove.

        Returns:
            None.

        Raises:
            KeyError: If the key does not exist in the dictionary.
        """

        del self._data[key]

    def __len__(self) -> int:
        """
        Return the number of key-value pairs in the dictionary.

        Returns:
            The number of key-value pairs in the dictionary as an integer.
        """
        return len(self._data)
