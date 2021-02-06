"""Implementation of a LinkedList"""


class LinkedList:
    """An implementation of a linked list data structure"""

    def __init__(self):
        self.__size = 0
        self.__head = None

    def append(self, item):
        """Append element"""

        if self.__size == 0:
            self.__head = Node(item, None)
        else:
            new_node = Node(item, None)
            last_node = self.__head

            for i in range(0, self.__size - 1):
                last_node = last_node.pointer

            last_node.pointer = new_node

        self.__size += 1

    def get(self, index):
        """Get element given index"""

        something = self.__head

        for i in range(0, index):
            something = something.pointer

        return something.value

    def delete(self, index):
        """Delete element given index"""

        if index == 0:
            self.__head = self.__head.pointer
        else:
            last_node = self.__head

            for i in range(0, index - 1):
                last_node = last_node.pointer

            last_node.pointer = last_node.pointer.pointer

        self.__size -= 1

    def size(self):
        """Get size of array"""

        return self.__size


class Node:

    def __init__(self, value, pointer):

        self.value = value
        self.pointer = pointer


# Testing
b = LinkedList()

b.append("a")
b.append("b")
b.append("c")
b.append("d")
b.delete(2)

print(', '.join(b.get(i) for i in range(b.size())))