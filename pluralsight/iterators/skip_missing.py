from itertools import *
from depth_first_in_order import InOrderIterator


missing = object()


class SkipMissingIterator:
    """Filters out missing nodes from synthetically-generated perfect trees.
    Wrapper around existing iterator.
    """

    def __init__(self, iterable):
        self._iterator = iter(iterable)

    def __next__(self):
        while True:
            item = next(self._iterator)
            if item is not missing:
                return item

    def __iter__(self):
        return self


expr_tree = ["+", "r", "*", missing, missing, "p", "q"]
iterator = SkipMissingIterator(expr_tree)
print(list(iterator))

iterator = SkipMissingIterator(InOrderIterator(expr_tree))
print(" ".join(iterator))
