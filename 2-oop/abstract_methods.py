from abc import ABCMeta, abstractmethod


class Sequence(metaclass=ABCMeta):
    """Our own version of collections.Sequence abstract base class."""

    @abstractmethod
    def __len__(self):
        """Return the length of the sequence"""

    @abstractmethod
    def __getitem__(self, i):
        """Returnn the element at index i of the sequence."""

    def __contains__(self, val):
        """Returns True if the val is found in the sequence; False otherwise."""
        for i in range(len(self)):
            if self[i] == val:
                return True
        return False

    def index(self, val):
        """Return leftmost index at which the val is found (or raise ValueError)"""
        for i in range(len(self)):
            if self[i] == val:
                return i
        raise ValueError('value not in sequence.')

    def count(self, val):
        """Return the number of elements equal to given value."""
        count = 0
        for i in range(len(self)):
            if self[i] == val:
                count += 1
        return count
