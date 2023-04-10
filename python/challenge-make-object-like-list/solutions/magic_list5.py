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

    def __getitem__(self, index: Union[int, slice]) -> Union[any, List[any]]:
        """
        Returns the value(s) at the given index or slice.

        Args:
            index (int or slice): Index or slice of the value(s) to retrieve.

        Returns:
            any or list: The value(s) at the given index or slice.
        """
        if isinstance(index, int):
            return self._data[index]
        elif isinstance(index, slice):
            return self._data[index.start : index.stop : index.step]

    def __setitem__(self, index: Union[int, slice], value: any) -> None:
        """
        Sets the value(s) at the given index or slice.

        Args:
            index (int or slice): Index or slice of the value(s) to set.
            value (any or list): The value(s) to set.

        Returns:
            None
        """
        if isinstance(index, int):
            self._data[index] = value
        elif isinstance(index, slice):
            self._data[index.start : index.stop : index.step] = value

    def __add__(self, other: List[any]) -> List[any]:
        """
        Concatenates the list with another list.

        Args:
            other (list): The list to concatenate with this list.

        Returns:
            list: The concatenated list.
        """
        add_lists = self._data + other
        return add_lists

    def __iadd__(self, other: List[any]) -> None:
        """
        Concatenates the list with another list in-place.

        Args:
            other (list): The list to concatenate with.

        Returns:
            None
        """
        self._data += other
        return self._data

    def __sub__(self, other: List[any]) -> List[any]:
        """
        Removes all occurrences of items from the second list in the first list.

        Args:
            other (list): The list of items to remove.

        Returns:
            list: The new list with items removed.
        """
        sub_list = [item for item in self._data if item not in other]
        return sub_list

    def __mul__(self, n: int) -> List[any]:
        """
        Repeats the list a certain number of times.

        Args:
            n (int): The number of times to repeat the list.

        Returns:
            list: The repeated list.
        """
        mul_list = self._data * n
        return mul_list

    def __lt__(self, other: "MagicList") -> bool:
        """
        Compares the items in the list for sorting.

        Args:
            other (MagicList): The list to compare with.

        Returns:
            bool: True if the first list is less than the second list, False otherwise.
        """

        return self._data < other._data

    def sort(self) -> None:
        """
        Sorts the list.

        Returns:
            None
        """
        self._data.sort()
