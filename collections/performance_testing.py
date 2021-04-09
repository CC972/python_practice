from itertools import count, islice
from sorted_frozen_set import SortedFrozenSet
from timeit import timeit


def recaman():
    """Generate Recaman's sequence."""

    seen = set()
    a = 0

    for n in count(1):
        yield a
        seen.add(a)
        c = a - n
        if c < 0 or c in seen:
            c = a + n
        a = c


print(f"First 1000 Recaman numbers: {list(islice(recaman(), 1000))}")

s = SortedFrozenSet(r for r in islice(recaman(), 1000) if r < 1000)
print(f"Recaman numbers which are less than 1000: {s}")
print(f"Number of Recaman numbers which are less than 1000: {len(s)}")

# Count number of occurrences of each number to spot missing numbers
[s.count(i) for i in range(1000)]

# Run list comprehension 200 times for performance benchmarking
print("Time taken: ", timeit(setup='from __ main__ import s', stmt='[s.count(i) for i in range(1000)]', number=200))
