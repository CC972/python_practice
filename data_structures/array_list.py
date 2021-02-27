"""Implementation of ArrayList"""


class ArrayList:
    """An implementation of a list data structure backed by an array"""

    def __init__(self, capacity=1):
        self.__array = [None] * capacity
        self.__size = 0

    def append(self, item):
        """Append element"""

        if len(self.__array) == self.__size:
            new_array = [None] * self.__size * 2

            for index in range(0, self.__size):
                new_array[index] = self.__array[index]

            self.__array = new_array

        self.__array[self.__size] = item
        self.__size += 1

    def get(self, index):
        """Get element given index"""

        if index < self.__size:
            return self.__array[index]
        else:
            raise Exception

    def delete(self, index):
        """Delete element given index"""

        for i in range(index, self.__size - 1):
            self.__array[i] = self.__array[i + 1]

        self.__size -= 1

    def size(self):
        """Get size of array"""

        return self.__size
