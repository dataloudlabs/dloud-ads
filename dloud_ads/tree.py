"""Abstract base class representing a tree structure."""

from .linked_queue import LinkedQueue

class Tree:
    """Abstract base class representing a tree structure."""

    class Position:
        """An abstraction representing the location of a single element within a tree.
        """

        def element(self):
            """Return the element stored at this Position."""
            raise NotImplementedError('must be implemented by subclass')

        def __eq__(self, other):
            """Return True if other Position represents the same location."""
            raise NotImplementedError('must be implemented by subclass')

        def __ne__(self, other):
            """Return True if other does not represent the same location."""
            return not self == other

    def root(self):
        """Return Position representing the tree's root (or None if empty)."""
        raise NotImplementedError('must be implemented by subclass')

    def parent(self, pos):
        """Return Position representing p's parent (or None if p is root)."""
        raise NotImplementedError('must be implemented by subclass')

    def num_children(self, pos):
        """Return the number of children that Position p has."""
        raise NotImplementedError('must be implemented by subclass')

    def children(self, pos):
        """Generate an iteration of Positions representing p's children."""
        raise NotImplementedError('must be implemented by subclass')

    def __len__(self):
        """Return the total number of elements in the tree."""
        raise NotImplementedError('must be implemented by subclass')

    def is_root(self, pos):
        """Return True if Position p represents the root of the tree."""
        return self.root() == pos

    def is_leaf(self, pos):
        """Return True if Position p does not have any children."""
        return self.num_children(pos) == 0

    def is_empty(self):
        """Return True if the tree is empty."""
        return len(self) == 0

    def depth(self, pos):
        """Return the number of levels separating Position p from the root."""
        if self.is_root(pos):
            return 0

        return 1 + self.depth(self.parent(pos))

    def _height1(self):
        """Return the height of the tree."""
        return max(self.depth(p) for p in self.positions() if self.is_leaf(p))

    def _height2(self, pos):
        """Return the height of the subtree rooted at Position p."""
        if self.is_leaf(pos):
            return 0

        return 1 + max(self._height2(c) for c in self.children(pos))

    def height(self, pos=None):
        """Return the height of the subtree rooted at Position p.

        If p is None, return the height of the entire tree.
        """
        if pos is None:
            pos = self.root()
        return self._height2(pos)

    def __iter__(self):
        """Generate an iteration of the tree's elements."""
        for pos in self.positions():
            yield pos.element()

    def positions(self):
        """Generate an iteration of the tree's positions."""
        return self.preorder()

    def preorder(self):
        """Generate a preorder iteration of positions in the tree."""
        if not self.is_empty():
            for pos in self._subtree_preorder(self.root()):
                yield pos

    def _subtree_preorder(self, pos):
        """Generate a preorder iteration of positions in subtree rooted at p."""
        yield pos
        for child in self.children(pos):
            for other in self._subtree_preorder(child):
                yield other

    def postorder(self):
        """Generate a postorder iteration of positions in the tree."""
        if not self.is_empty():
            for pos in self._subtree_postorder(self.root()):
                yield pos

    def _subtree_postorder(self, pos):
        """Generate a postorder iteration of positions in subtree rooted at p."""
        for child in self.children(pos):
            for other in self._subtree_postorder(child):
                yield other
        yield pos

    def breadthfirst(self):
        """Generate a breadth-first iteration of the positions of the tree."""
        if not self.is_empty():
            fringe = LinkedQueue()
            fringe.enqueue(self.root())
            while not fringe.is_empty():
                pos = fringe.dequeue()
                yield pos
                for child in self.children(pos):
                    fringe.enqueue(child)
