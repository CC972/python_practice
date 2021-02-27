class HashMap:
    """Implementation of a HashMap using chaining strategy.
    Simple Python dictionary where each row in the backing array contains the head to a LinkedList."""

    def __init__(self, capacity=3, loading_factor=1):
        self.__size = 0
        self.__capacity = capacity
        self.__loading_factor = loading_factor  # Maximum size of capacity to size of any LinkedList
        self.__array = [None] * capacity

    def get(self, key):
        """Get value corresponding to key"""

        # Determine bucket to which entry belongs
        bucket_index = hash(key) % self.__capacity

        # Find first node in bucket
        node = self.__array[bucket_index]

        # Iterate through LinkedList of nodes in bucket
        while node:
            if node.key == key:
                return node.value
            node = node.next_node

    def contains(self, key):
        """Check if entry exists"""

        return self.get(key) is not None

    def assign(self, key, value):
        """Add new entry if key doesn't already exist, otherwise update existing entry"""

        bucket_index = hash(key) % self.__capacity
        node = head = self.__array[bucket_index]

        while node:
            # Update value if key already exists
            if node.key == key:
                node.value = value
                return
            node = node.next_node

        # Otherwise add new entry at the beginning of the LinkedList (i.e. array itself)
        self.__array[bucket_index] = Node(key, value, head)
        self.__size += 1

    def remove(self, key):
        """Delete entry"""

        bucket_index = hash(key) % self.__capacity
        node = self.__array[bucket_index]

        # If first node is being removed
        if node and node.key == key:
            self.__array[bucket_index] = node.next_node
            self.__size -= 1
            return

        while node:

            next_node = node.next_node

            if next_node.key == key:
                node.next_node = next_node.next_node
                self.__size -= 1
                return

    def __str__(self):
        """Convert HashMap object into readable object"""

        hash_map_string = ""

        for index, node in enumerate(self.__array):

            chain = []
            while node:
                chain.append("(" + str(node.key) + ", " + str(node.value) + ")")
                node = node.next_node

            hash_map_string += str(index) + ": " + ", ".join(chain) + "\n"

        return hash_map_string


class Node:
    """Implementation of a node, which consists of a key-value pair, and a pointer to the next node"""

    def __init__(self, key, value, next_node):
        self.key = key
        self.value = value
        self.next_node = next_node
