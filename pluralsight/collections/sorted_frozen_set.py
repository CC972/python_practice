from _collections_abc import Sequence
from bisect import bisect_left
from itertools import chain


# Inherit from Sequence to inherit mix-in methods index and count
# This is later overrided by a more efficient custom implementation, but is kept here for demonstration purposes


class SortedFrozenSet(Sequence):

    def __init__(self, items=None):
        self._items = tuple(sorted(
            set(items) if (items is not None)
            else set()
        ))

    def __contains__(self, item):
        """Override inherited method from Sequence.
        Use binary search to improve time complexity from O(n) to O(log(n))."""

        index = bisect_left(self._items, item)
        return (index != len(self._items)) and self._items[index] == item

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index):
        result = self._items[index]
        return (
            SortedFrozenSet(result)
            if isinstance(index, slice)
            else result
        )

    def __repr__(self):
        return "{type}({arg})".format(
            type=type(self).__name__,
            arg=(
                "[{}]".format(
                    ", ".join(
                        map(repr, self._items)
                    )
                )
                if self._items else ""
            )
        )

    def __eq__(self, rhs):
        if not isinstance(rhs, type(self)):
            return NotImplemented
        return self._items == rhs._items

    def __hash__(self):
        return hash(
            (type(self), self._items)
        )

    def __add__(self, rhs):
        if not isinstance(rhs, type(self)):
            return NotImplemented
        return SortedFrozenSet(
            chain(self._items, rhs._items)
        )

    def __mul__(self, rhs):
        """Repetition does not apply to a SortedFrozenSet since the elements must be unique.
        So either return original or empty SortedFrozenSet."""

        return self if rhs > 0 else SortedFrozenSet()  # Can return self since SortedFrozenSet is immutable

    def __rmul__(self, lhs):
        """Delegates to __mul__ through the high-level infix operator syntax"""

        return self * lhs

    def count(self, item):
        """Delegate to optimised __contains__ method"""

        return int(item in self)

    def index(self, item):
        """Override inherited index method"""

        index = bisect_left(self._items, item)
        if (index != len(self._items)) and self._items[index] == item:
            return index
        raise ValueError(f"{item!r} not found")