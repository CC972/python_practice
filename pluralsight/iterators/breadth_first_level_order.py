from itertools import *
from iterator_utils import _is_perfect_length


class LevelOrderIterator:

    def __init__(self, sequence):
        # Guard clause
        if not _is_perfect_length(sequence):
            raise ValueError(
                f"Sequence of length {len(sequence)} does not represent "
                "a perfect binary tree with length 2ⁿ - 1"
            )
        self._sequence = sequence
        self._index = 0

    def __next__(self):
        if self._index >= len(self._sequence):
            raise StopIteration
        result = self._sequence[self._index]
        self._index += 1
        return result

    def __iter__(self):
        return self


expr_tree = ["*", "+", "-", "a", "b", "c", "d"]

iterator = LevelOrderIterator(expr_tree)
print(next(iterator))

iterator = LevelOrderIterator(expr_tree)
print(" ".join(iterator))

# Using dictionary comprehension to test perfect length
print({i: _is_perfect_length(["x"] * i) for i in range(0, 32)})

# Test guard clause using sequence with 4 elements
non_tree = "+ 24 12 -".split()
iterator = LevelOrderIterator(non_tree)