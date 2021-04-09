from itertools import *
from skip_missing import SkipMissingIterator, missing
from depth_first_in_order import InOrderIterator


class TranslationIterator:

    def __init__(self, table, iterable):
        self._table = table
        self._iterator = iter(iterable)

    def __next__(self):
        item = next(self._iterator)
        return self._table.get(item, item)

    def __iter__(self):
        return self


typesetting_table = {
    "-" : "−",
    "* ": "×",
    "/" : "÷",
}

m = missing

expr_tree = [
                "-",
          "*",         "/",
     "p",     "q", "r",    "+",
    m,  m,  m,  m, m, m, "s", "t"
]

iterator = TranslationIterator(
    typesetting_table,
    SkipMissingIterator(InOrderIterator(expr_tree))
)
print(" ".join(iterator))
