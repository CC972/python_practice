class DoublyLinkedList:

    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def get(self, index):
        if index >= self.__size:
            raise Exception
        node = self.__get_node(index)
        return node.value

    def append(self, item):
        new_node = Node(item, self.__tail, None)

        if self.__head is None:
            self.__head = new_node
            self.__tail = new_node
        else:
            self.__tail.next = new_node
            self.__tail = new_node

        self.__size += 1

    def delete(self, index):
        if index >= self.__size:
            raise Exception

        node = self.__get_node(index - 1)

        if node.next.next is not None:
            node.next.next.prev = node

        node.next = node.next.next

        self.__size -= 1

    def size(self):
        return self.__size

    def __get_node(self, index):
        mid = self.__size // 2

        if index < mid:
            node = self.__head
            for _ in range(index):
                node = node.next
        else:
            node = self.__tail
            for _ in range(self.__size - 1, index, -1):
                node = node.prev

        return node


class Node:
    def __init__(self, value, prev, next):
        self.value = value
        self.prev = prev
        self.next = next
