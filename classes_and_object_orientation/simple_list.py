class SimpleList:

    def __init__(self, items):
        self._items = list(items)

    def add(self, item):
        self._items.append(item)

    def __getitem__(self, index):
        return self._items[index]

    def sort(self):
        self._items.sort()

    def __len__(self):
        return len(self._items)

    def __repr__(self):
        return f'{type(self).__name__}({self._items!r})'


class SortedList(SimpleList):

    def __init__(self, items=()):
        super().__init__(items)
        self.sort()

    def add(self, item):
        super().add(item)
        self.sort()


class IntList(SimpleList):

    def __init__(self, items=()):
        for x in items:
            self._validate(x)
        super().__init__(items)

    @staticmethod
    def _validate(x):
        if not isinstance(x, int):
            raise TypeError('IntList only supports integer values.')

    def add(self, item):
        self._validate(item)
        super().add(item)


# Multiple inheritance
class SortedIntList(IntList, SortedList):
    pass


# Testing out SortedList
sl = SortedList([4, 3, 78, 1])
print(sl)
print(len(sl))
sl.add(-42)
print(sl)

# Returns true for both
print(isinstance(sl, SortedList))
print(isinstance(sl, SimpleList))

# isinstance can also accept tuple as second argument
# Returns true if first argument is an instance of any of the types in the tuple
y = []
print(isinstance(y, (float, dict, list)))

# Testing out IntList
il = IntList([1, 2, 3, 4])
il.add(21)
# il.add("12")  # Error

# Using issubclass()
print(issubclass(IntList, SimpleList))
print(issubclass(SortedList, SimpleList))
print(issubclass(SortedList, IntList))

# Testing out SortedIntList
# Both IntList and SortedList override the add method
# Yet SortedIntList can maintain behaviours from both
# Because super() uses the full MRO of an object, not just the base classes from a class definition
sil = SortedIntList([42, 23, 3])
print(sil)
sil.add(12)
print(sil)

# Using __bases__
print(SortedIntList.__bases__)

# Method Resolution Order (MRO)
# Ordering of inheritance graph that determines which implementation to use when invoking a method
# Calling add() on instance of SortedIntList results in calling super()
# The first class in the MRO after SortedIntList which implements add() is IntList
# However the super() call in IntList.add() uses the full MRO of SortedIntList
# Meaning it actually resolves to SortedList.add(), instead of SimpleList.add()
# This is how SortedIntList maintains both constraints
print(SortedIntList.__mro__)
print(IntList.__mro__)
