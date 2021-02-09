from itertools import *
from pluralsight.iterators.depth_first_pre_order import PreOrderIterator
from pluralsight.iterators.iterator_utils import _is_perfect_length
from pluralsight.iterators.skip_missing import SkipMissingIterator


class PerfectBinaryTree:
    """Encapsulate sequence inside collection"""

    def __init__(self, breadth_first_items):
        # Binary tree flattened breadth-first in an iterable series of items
        self._sequence = tuple(breadth_first_items)  # Immutable, shallow copy of source data
        if not _is_perfect_length(self._sequence):
            raise ValueError(
                f"Sequence of length {len(self._sequence)} does not represent "
                "a perfect binary tree with length 2ⁿ - 1"
            )

    def __iter__(self):
        # Wrapper around sequence, minimal interface for iterable
        return SkipMissingIterator(PreOrderIterator(self._sequence))


tree = PerfectBinaryTree("+ * / u v w x".split())
iterator = iter(tree)

print(next(iterator))
print(" ".join(tree))

for item in tree:
    print(item)