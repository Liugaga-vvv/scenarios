class MyIterator:
    """A class that implements an iterator that iterates from start to end (inclusive)"""

    def __init__(self, start: int, end: int):
        """Initialize the iterator with two integer arguments start and end (0 <= start <= end).The iterator will iterate from start to end (inclusive).

        Args:
            start(int): An integer,e.g. 2
            end(int): An integer,e.g. 8
        """
        # TODO: implement this function
        # Note: Do not change the existing code

        self.start = None
        self.end = None
        self.current = None

    def __next__(self) -> int:
        """Return the next value from the iteration. Return None when the iteration has ended.

        Args:
            self: the iterator object

        Returns:
            value: the next value(int) from the iteration, or None when the iteration has ended
        """
        # TODO: implement this function
        # Note: Do not change the existing code

        if self.current <= None:
            value = None
            self.current = None
            return value
        else:
            return None

    def __iter__(self) -> "MyIterator":
        """Return the iterator object itself.

        Args:
            self: the iterator object

        Returns:
            the iterator object itself
        """
        # TODO: implement this function
        # Note: Do not change the existing code

        return None
