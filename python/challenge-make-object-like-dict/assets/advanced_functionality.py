from typing import Any, List, Iterator


class DictLikeObject:
    """
    A class that behaves like a dictionary using magic methods.
    """

    def __init__(self):

        # TODO

        pass

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

        # TODO

        return

    def __setitem__(self, key: str, value: Any) -> None:
        """
        Set the value for a given key using square bracket notation.

        Args:
            key: The key to set the value for.
            value: The value to set.

        Returns:
            None.
        """

        # TODO

        pass

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

        # TODO

    def __len__(self) -> int:
        """
        Return the number of key-value pairs in the dictionary.

        Returns:
            The number of key-value pairs in the dictionary as an integer.
        """

        # TODO

        return

    def __contains__(self, key: str) -> bool:
        """
        Check if a key exists in the dictionary.

        Args:
            key: The key to check.

        Returns:
            True if the key exists in the dictionary, False otherwise.
        """

        # TODO

        return

    def __iter__(self) -> Iterator:
        """
        Allow for iteration over keys in the dictionary using a for loop.

        Returns:
            An iterator over keys in the dictionary.
        """

        # TODO

        return

    def keys(self) -> List[str]:
        """
        Return a list of keys in the dictionary.

        Returns:
            A list of keys in the dictionary.
        """

        # TODO

        return
