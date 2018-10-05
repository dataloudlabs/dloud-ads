"""Linked representation of a binary tree structure."""

from .binary_tree import BinaryTree

class LinkedBinaryTree(BinaryTree):
    """Linked representation of a binary tree structure."""

    class _Node:
        """Lightweight, nonpublic class for storing a node."""
        __slots__ = '_element', '_parent', '_left', '_right'

        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    class Position(BinaryTree.Position):
        """An abstraction representing the location of a single element."""

        def __init__(self, container, node):
            """Constructor should not be invoked by user."""
            self._container = container
            self._node = node

        def element(self):
            """Return the element stored at this Position."""
            return self._node._element

        def __eq__(self, other):
            """Return True if other is a Position representing the same
            location."""
            return type(other) is type(self) and other._node is self._node

    def _validate(self, pos):
        """Return associated node, if position is valid."""
        if not isinstance(pos, self.Position):
            raise TypeError('p must be proper Position type')
        if pos._container is not self:
            raise ValueError('p does not belong to this container')
        if pos._node._parent is pos._node:
            raise ValueError('p is no longer valid')
        return pos._node

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

    def parent(self, pos):
        """Return the Position of p's parent (or None if p is root)."""
        node = self._validate(pos)
        return self._make_position(node._parent)

    def left(self, pos):
        """Return the Position of p's left child (or None if no left child)."""
        node = self._validate(pos)
        return self._make_position(node._left)

    def right(self, pos):
        """Return the Position of p's right child (or None if no right child)"""
        node = self._validate(pos)
        return self._make_position(node._right)

    def num_children(self, pos):
        """Return the number of children of Position p."""
        node = self._validate(pos)
        count = 0
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1
        return count

    def _add_root(self, elem):
        """Place element e at the root of an empty tree and return new Position.

        Raise ValueError if tree nonempty.
        """
        if self._root is not None:
            raise ValueError('Root exists')
        self._size = 1
        self._root = self._Node(elem)
        return self._make_position(self._root)

    def _add_left(self, pos, elem):
        """Create a new left child for Position p, storing element e.

        Return the Position of new node.
        Raise ValueError if Position p is invalid or p already has a left child.
        """
        node = self._validate(pos)
        if node._left is not None:
            raise ValueError('Left child exists')
        self._size += 1
        node._left = self._Node(elem, node)
        return self._make_position(node._left)

    def _add_right(self, pos, elem):
        """Create a new right child for Position pos, storing element elem.

        Return the Position of new node.
        Raise ValueError if Position pos is invalid or pos already has
        a right child.
        """
        node = self._validate(pos)
        if node._right is not None:
            raise ValueError('Right child exists')
        self._size += 1
        node._right = self._Node(elem, node)
        return self._make_position(node._right)

    def _replace(self, pos, elem):
        """Replace the element at position p with e, and return old element."""
        node = self._validate(pos)
        old = node._element
        node._element = elem
        return old

    def _delete(self, pos):
        """Delete the node at Position p, and replace it with its child, if any.

        Return the element that had been stored at Position p.
        Raise ValueError if Position p is invalid or p has two children.
        """
        node = self._validate(pos)
        if self.num_children(pos) == 2:
            raise ValueError('Position has two children')
        child = node._left if node._left else node._right
        if child is not None:
            child._parent = node._parent
        if node is self._root:
            self._root = child
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size -= 1
        node._parent = node
        return node._element

    def _attach(self, pos, tree1, tree2):
        """Attach trees tree1 and tree2, respectively, as the left and right
        subtrees of the external Position p.

        As a side effect, set tree1 and tree2 to empty.
        Raise TypeError if trees tree1 and tree2 do not match type of this tree.
        Raise ValueError if Position p is invalid or not external.
        """
        node = self._validate(pos)
        if not self.is_leaf(pos):
            raise ValueError('position must be leaf')
        if not type(self) is type(tree1) is type(tree2):
            raise TypeError('Tree types must match')
        self._size += len(tree1) + len(tree2)
        if not tree1.is_empty():
            tree1._root._parent = node
            node._left = tree1._root
            tree1._root = None
            tree1._size = 0
        if not tree2.is_empty():
            tree2._root._parent = node
            node._right = tree2._root
            tree2._root = None
            tree2._size = 0
