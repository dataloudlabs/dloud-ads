"""Abstract base class representing a binary tree structure."""

from .tree import Tree

class BinaryTree(Tree):
    """Abstract base class representing a binary tree structure."""

    def left(self, pos):
        """Return a Position representing p's left child.

        Return None if p does not have a left child.
        """
        raise NotImplementedError('must be implemented by subclass')

    def right(self, pos):
        """Return a Position representing p's right child.

        Return None if p does not have a right child.
        """
        raise NotImplementedError('must be implemented by subclass')

    def sibling(self, pos):
        """Return a Position representing p's sibling (or None if no sibling)."""
        parent = self.parent(pos)
        if parent is None:
            return None

        if pos == self.left(parent):
            return self.right(parent)

        return self.left(parent)

    def children(self, pos):
        """Generate an iteration of Positions representing p's children."""
        if self.left(pos) is not None:
            yield self.left(pos)
        if self.right(pos) is not None:
            yield self.right(pos)

    def inorder(self):
        """Generate an inorder iteration of positions in the tree."""
        if not self.is_empty():
            for pos in self._subtree_inorder(self.root()):
                yield pos

    def _subtree_inorder(self, pos):
        """Generate an inorder iteration of positions in subtree rooted at p."""
        if self.left(pos) is not None:
            for other in self._subtree_inorder(self.left(pos)):
                yield other
        yield pos
        if self.right(pos) is not None:
            for other in self._subtree_inorder(self.right(pos)):
                yield other

    def positions(self):
        """Generate an iteration of the tree's positions."""
        return self.inorder()
