from priority_queue_ABC import PriorityQueueBase
from positional_list import PositionalList


class Empty(Exception):
    pass


class UnsortedPriorityQueue(PriorityQueueBase):
    """A min-oriented priority queue implemented with an unsorted list."""

    def _find_min(self):
        """Return Position of item with minimum key."""
        if self.is_empty():
            raise Empty("Priority Queue is empty")
        small = self._data.first()
        walk = self._data.after(small)
        while walk is not None:
            if walk.element() < small.element():
                small = walk
            walk = self._data.after(walk)
        return small
