from typing import Iterator


class magic_set:
    """
    A class that behaves like a set using magic methods.

    Methods:
    __init__: Initializes an empty set.
    __str__: Returns a string representation of the set.
    __len__: Returns the number of elements in the set.
    __contains__: Checks if an element is in the set.
    __iter__: Iterates over the set.
    __next__: Returns the next element in the iteration.
    __eq__: Checks if two sets are equal.
    __ne__: Checks if two sets are not equal.
    __and__: Returns the intersection of two sets.
    __or__: Returns the union of two sets.
    __sub__: Returns the difference of two sets.
    """

    def __init__(self) -> None:
        """Initializes an empty set."""
        self._index = 0
        self._data = []

    def add(self, item: object) -> None:
        """Adds an element to the set."""
        if item not in self._data:
            self._data.append(item)

    def remove(self, item: object) -> None:
        """Removes an element from the set."""
        if item in self._data:
            self._data.remove(item)

    def clear(self) -> None:
        """Removes all elements from the set."""
        self._data.clear()

    def __str__(self) -> str:
        """Returns a string representation of the set."""
        return f"{set(self._data)}"

    def __len__(self) -> int:
        """Returns the number of elements in the set."""
        return len(self._data)

    def __contains__(self, item: object) -> bool:
        """Checks if an element is in the set."""
        return item in self._data

    def __iter__(self) -> Iterator:
        """Iterates over the set."""
        return self

    def __next__(self) -> object:
        """Returns the next element in the iteration."""
        if self._index >= len(self._data):
            raise StopIteration
        result = self._data[self._index]
        self._index += 1
        return result

    def __eq__(self, other: object) -> bool:
        """Checks if two sets are equal."""
        if not isinstance(other, magic_set):
            return NotImplemented
        return set(self._data) == set(other._data)

    def __ne__(self, other: object) -> bool:
        """Checks if two sets are not equal."""
        if not isinstance(other, magic_set):
            return NotImplemented
        return set(self._data) != set(other._data)

    def __and__(self, other: object) -> "magic_set":
        """Returns the intersection of two sets."""
        if not isinstance(other, magic_set):
            return NotImplemented
        result = magic_set()
        for item in self._data:
            if item in other._data:
                result.add(item)
        return result

    def __or__(self, other: object) -> "magic_set":
        """Returns the union of two sets."""
        if not isinstance(other, magic_set):
            return NotImplemented
        result = magic_set()
        for item in self._data:
            result.add(item)
        for item in other._data:
            result.add(item)
        return result

    def __sub__(self, other: object) -> "magic_set":
        """Returns the difference of two sets."""
        if not isinstance(other, magic_set):
            return NotImplemented
        result = magic_set()
        for item in self._data:
            if item not in other._data:
                result.add(item)
        return result
