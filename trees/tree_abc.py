from abc import ABCMeta, abstractmethod


class Tree(metaclass=ABCMeta):
    """Abstract base class representing a tree structure."""

    # --------------------------- nested Position class ------------------------
    class Position:
        """An abstraction representing the location of a single element."""

        @abstractmethod
        def element(self):
            """Return the element stored at this position."""

        @abstractmethod
        def __eq__(self, other):
            """Return True if other Position represents same location."""

        def __ne__(self, other):
            """Return True if other does not represent same location."""
            return not (self == other)

    @abstractmethod
    def root(self):
        """Return Position representing the tree's root (or None if empty)."""

    @abstractmethod
    def parent(self, p):
        """Return Position representing p's parent (or None if p is root)."""

    @abstractmethod
    def num_children(self, p):
        """Return the number of children that Position p has."""

    @abstractmethod
    def children(self, p):
        """Generate an iteration of Positions representing p's children."""

    @abstractmethod
    def __len__(self):
        """Return the total number of elements in the tree."""

    def is_root(self, p):
        """Return True if Position p represents the root of the tree."""
        return self.root() == p

    def is_leaf(self, p):
        """Return True if Position p does not have any children."""
        return self.num_children(p) == 0

    def is_empty(self):
        """Return True if the tree is empty."""
        return len(self) == 0
