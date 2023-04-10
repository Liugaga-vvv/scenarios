class ReverseIterator:
    """A class that implements an iterator that iterates over the elements of data in reverse order"""

    def __init__(self, data: list):
        """Initialize the iterator with a list of integers data.

        Args:
            data(list):A list of integers data, e.g. [1,2,3,4,5]
        """
        # TODO: implement this function
        # Note: Do not change the existing code

        self.data = None
        self.index = None

    def __next__(self) -> int:
        """Return the next value from the iteration. Return None when the iteration has ended.

        Args:
            self: the iterator object

        Returns:
            value(int): the next value from the iteration, or None when the iteration has ended
        """
        # TODO: implement this function
        # Note: Do not change the existing code

        if self.index >= None:
            value = None
            self.index = None
            return value
        else:
            return None

    def __iter__(self) -> "ReverseIterator":
        """Return the iterator object itself.

        Args:
            self: the iterator object

        Returns:
            the iterator object itself
        """
        # TODO: implement this function
        # Note: Do not change the existing code

        return None
