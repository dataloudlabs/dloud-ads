"""A sequential container of elements allowing positional access."""

from .doubly_linked_base import _DoublyLinkedBase

class PositionalList(_DoublyLinkedBase):
    """A sequential container of elements allowing positional access."""
    class Position:
        """An abstraction representing the location of a single element.

        Note that two position instaces may represent the same inherent
        location in the list.  Therefore, users should always rely on
        syntax 'p == q' rather than 'p is q' when testing equivalence of
        positions.
        """

        def __init__(self, container, node):
            """Constructor should not be invoked by user."""
            self._container = container
            self._node = node

        def element(self):
            """Return the element stored at this Position."""
            return self._node._element

        def __eq__(self, other):
            """Return True if other is a Position representing the same location."""
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            """Return True if other does not represent the same location."""
            return not self == other

    def _validate(self, pos):
        """Return position's node, or raise appropriate error if invalid."""
        if not isinstance(pos, self.Position):
            raise TypeError('p must be proper Position type')
        if pos._container is not self:
            raise ValueError('p does not belong to this container')
        if pos._node._next is None:
            raise ValueError('p is no longer valid')
        return pos._node

    def _make_position(self, node):
        """Return Position instance for given node (or None if sentinel)."""
        if node is self._header or node is self._trailer:
            return None

        return self.Position(self, node)

    def first(self):
        """Return the first Position in the list (or None if list is empty)."""
        return self._make_position(self._header._next)

    def last(self):
        """Return the last Position in the list (or None if list is empty)."""
        return self._make_position(self._trailer._prev)

    def before(self, pos):
        """Return the Position just before Position p (or None if p is first)."""
        node = self._validate(pos)
        return self._make_position(node._prev)

    def after(self, pos):
        """Return the Position just after Position p (or None if p is last)."""
        node = self._validate(pos)
        return self._make_position(node._next)

    def __iter__(self):
        """Generate a forward iteration of the elements of the list."""
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    def _insert_between(self, elem, predecessor, successor):
        """Add element between existing nodes and return new Position."""
        node = _DoublyLinkedBase._insert_between(self, elem, predecessor, successor)
        return self._make_position(node)

    def add_first(self, element):
        """Insert element e at the front of the list and return new Position."""
        return self._insert_between(element, self._header, self._header._next)

    def add_last(self, element):
        """Insert element e at the back of the list and return new Position."""
        return self._insert_between(element, self._trailer._prev, self._trailer)

    def add_before(self, pos, elem):
        """Insert element e into list before Position p and return new Position."""
        original = self._validate(pos)
        return self._insert_between(elem, original._prev, original)

    def add_after(self, pos, elem):
        """Insert element e into list after Position p and return new Position."""
        original = self._validate(pos)
        return self._insert_between(elem, original, original._next)

    def delete(self, pos):
        """Remove and return the element at Position p."""
        original = self._validate(pos)
        return self._delete_node(original)

    def replace(self, pos, elem):
        """Replace the element at Position p with e.

        Return the element formerly at Position p.
        """
        original = self._validate(pos)
        old_value = original._element
        original._element = elem
        return old_value
