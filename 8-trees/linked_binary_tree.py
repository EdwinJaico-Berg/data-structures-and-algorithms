from binary_tree import BinaryTree


class LinkedBinaryTree(BinaryTree):
    """Linked representation of a binary tree structure."""

    class _Node:

        __slots__ = '_element', '_parent', '_left', '_right'

        def __init__(self, element=None, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    class Position(BinaryTree.Position):
        """An abstraction representing the location of a single element."""

        def __init__(self, container, node):
            """Constructor should not be invoked by user."""
            self._container = container         # container will be the instance of binary tree
            self._node = node

        def element(self):
            """Return the element stored at this Position."""
            return self._node._element

        def __eq__(self, other):
            """Return True if other is a Position representing the same location."""
            return type(other) is type(self) and other._node is self._node

    def _validate(self, p):
        """Return the associated node, if position is valid."""
        if not isinstance(p, self.Position):
            raise TypeError('p must ve proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._parent is p._node:      # convention for deprecated nodes
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        """Return Position instance for given node (or None if no node)."""
        return self.Position(self, node) if node is not None else None

    def __init__(self):
        """Create an initially empty binary tree."""
        self._root = None
        self._size = 0

    def __len__(self):
        """Return the total number of elements in the tree."""
        return self._size

    def root(self):
        """Return the root Position of the tree (or None if tree is empty)."""
        return self._make_position(self._root)

    def parent(self, p):
        """Return the Position of p's parent (or None if p is root)."""
        node = self._validate(p)
        return self._make_position(node._parent)

    def left(self, p):
        """Return the Position of p's left child (or None if no left child)."""
        node = self._validate(p)
        return self._make_position(node._left)

    def right(self, p):
        """Return the Position of p's right child (or None if no right child)."""
        node = self._validate(p)
        return self._make_position(node._right)

    def num_children(self, p):
        """Return the number of children of Position p."""
        node = self._validate(p)
        count = 0
        if node._left:
            count += 1
        if node._right:
            count += 1
        return count

    def _add_root(self, e):
        """Place element e at the root of an empty tree and retun new Position.

        Raise ValueError if tree is nonempty.
        """
        if self._root:
            raise ValueError('Root exists')
        self._size = 1
        self._root = self._Node(e)
        return self._make_position(self._root)

    def _add_left(self, p, e):
        """Create a new left child for Position p, storing element e.

        Return the Position of new node.
        Raise ValueError if Position p is invalid or p already has a left child.
        """
        node = self._validate(p)
        if node._left:
            raise ValueError('Left child exists')
        self._size += 1
        node._left = self._Node(e, node)
        return self._make_position(node._left)

    def _add_right(self, p, e):
        """Create a new right child for Position p, storing element e.

        Return the Position of new node.
        Raise ValueError if Position p is invalid or p already has a right child.
        """
        node = self._validate(p)
        if node._right:
            raise ValueError('Left child exists')
        self._size += 1
        node._right = self._Node(e, node)
        return self._make_position(node._right)

    def _replace(self, p, e):
        """Replace the element at Position p with e, and return old element."""
        node = self._validate(p)
        old = node._element
        node._element = e
        return old

    def _delete(self, p):
        """Delete the node at Position p, and replace with its child, if any.

        Return the element that had been stored at Position p.
        Raise ValueError if Position p is invalid or p has two children.
        """
        node = self._validate(p)
        if self.num_children(p) == 2:
            raise ValueError('p has two children')
        child = node._left if node._left else node._right
        if child:
            child._parent = node._parent
        # if the node is the root, we replace the root
        if node is self._root:
            self._root = child
        # if this is not the case, we need to reassign the left or right node
        # of the parent
        else:
            parent = node._parent
            if node is parent._left:        # check whether the node was left
                parent._left = child
            else:                           # node was right child of parent
                parent._right = child
        self._size -= 1
        node._parent = node                 # convention for deprecated nodes
        return node._element

    def _attach(self, p, t_left, t_right):
        """Attach trees t_left and t_right as left and right subtrees of external p."""
        node = self._validate(p)
        if not self.is_leaf(p):
            raise ValueError('position must be leaf')
        if not type(self) is type(t_left) is type(t_right):
            raise TypeError('Tree types must match')
        self._size += len(t_left) + len(t_right)
        if not t_left.is_empty():
            t_left._root._parent = node
            node._left = t_left._root
            t_left._root = None                 # set tree instance to empty
            t1._size = 0
        if not t_right.is_empty():
            t_right._root._parent = node
            node._right = t_right._root
            t_right._root = None
            t_right._size = 0


