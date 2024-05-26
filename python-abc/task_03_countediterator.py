#!/usr/bin/python3
class CountedIterator:
    """A class that extends the built-in iterator to count iterations.

    This iterator keeps track of the number of items iterated over. It overrides
    the __next__ method to increment a counter each time an item is fetched.

    Attributes:
        iterator: The iterator object obtained using the iter function.
        count (int): Counter to track the number of items iterated.

    Methods:
        __init__(some_iterable):
            Initializes the CountedIterator with an iterator object and sets the
            counter to zero.

        get_count():
            Returns the current value of the counter.

        __next__():
            Overrides the __next__ method of the iterator. Increments the counter
            each time an item is fetched and returns the next item. Raises
            StopIteration if there are no more items left to iterate.
    """

    def __init__(self, some_iterable):
        """Initializes the CountedIterator.

        Args:
            some_iterable (iterable): Any iterable object (e.g., list, tuple).
        """
        self.iterator = iter(some_iterable)
        self.count = 0

    def get_count(self):
        """Returns the current value of the counter."""
        return self.count

    def __next__(self):
        """Returns the next item from the iterator and increments the counter."""
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration("No more items to iterate")
