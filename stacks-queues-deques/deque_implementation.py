from stack_implementation import Empty


class ArrayDeque:
    """Deque implementation using a Python list as underlying storage."""
    DEFAULT_CAPACITY = 10

    def __init__(self):
        """Create an empty deque"""
        self._data = [None] * self.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        """Return the length of the deque."""
        return self._size

    def is_empty(self):
        """True if the queue is empty; otherwise False."""
        return self._size == 0

    def add_first(self, e):
        """Add element e to the front of the deque."""
        if self.size == len(self._data):
            self._resize(2 * len(self._data))
        self._front = (self._front - 1) % len(self._data)
        self._data[self._front] = e
        self._size += 1

    def add_last(self, e):
        """Add element, e, to the back of the deque."""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def delete_first(self):
        """Remove and return the first element from the deque.

        Raise Empty exception if the deque is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1

        # resize the underlying list
        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)

        return answer

    def delete_last(self, e):
        """Remove and return the last element from the deque.

        Raise Empty exception if the deque is empty.
        """
        if self.is_empty():
            raise Empty
        back = (self._front + self._size - 1) % len(self._data)
        answer = self._data[back]
        self._data[back] = None
        self._size -= 1

        # resize the underlying list
        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)

        return answer

    def first(self):
        """Return but do not remove the element at the front of the deque.

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('deque is empty')
        return self._data[self._front]

    def last(self):
        """Return but do not remove the element at the back of the deque.

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('deque is empty')
        back = (self._front + self._size - 1) % len(self._data)
        return self._data[back]

    def _resize(self, cap):
        """Resize to a new list of capacity >= len(self)."""
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (walk + 1) % len(old)
        self._front = 0

