class MyIterator:
    """A class that implements an iterator that iterates from start to end (inclusive)"""

    def __init__(self, start: int, end: int):
        """Initialize the iterator with two integer arguments start and end (0 <= start <= end).The iterator will iterate from start to end (inclusive).

        Args:
            start(int): An integer,e.g. 2
            end(int): An integer,e.g. 8
        """
        self.start = start
        self.end = end
        self.current = start

    def __next__(self) -> int:
        """Return the next value from the iteration. Return None when the iteration has ended.

        Args:
            self: the iterator object

        Returns:
            value(int): the next value from the iteration, or None when the iteration has ended
        """
        if self.current <= self.end:
            value = self.current
            self.current += 1
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
        return self
