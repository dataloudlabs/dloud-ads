"""Double-ended queue implementation based on a doubly linked list."""

from .doubly_linked_base import _DoublyLinkedBase


class LinkedDeque(_DoublyLinkedBase):
    """Double-ended queue implementation based on a doubly linked list."""

    def first(self):
        """Return (but do not remove) the element at the front of the deque.

        Raise ValueError exception if the deque is empty.
        """
        if self.is_empty():
            raise ValueError("Deque is empty")
        return self._header._next._element

    def last(self):
        """Return (but do not remove) the element at the back of the deque.

        Raise ValueError exception if the deque is empty.
        """
        if self.is_empty():
            raise ValueError("Deque is empty")
        return self._trailer._prev._element

    def insert_first(self, elem):
        """Add an element to the front of the deque."""
        self._insert_between(elem, self._header, self._header._next)

    def insert_last(self, elem):
        """Add an element to the back of the deque."""
        self._insert_between(elem, self._trailer._prev, self._trailer)

    def delete_first(self):
        """Remove and return the element from the front of the deque.

        Raise ValueError exception if the deque is empty.
        """
        if self.is_empty():
            raise ValueError("Deque is empty")
        return self._delete_node(self._header._next)

    def delete_last(self):
        """Remove and return the element from the back of the deque.

        Raise ValueError exception if the deque is empty.
        """
        if self.is_empty():
            raise ValueError("Deque is empty")
        return self._delete_node(self._trailer._prev)
