class _Node:
    """Lightweight, non-public class for storing a singly linked node."""
    __slots__ = '_element', '_next'

    def __init__(self, element, next):
        self._element = element
        self._next = next
