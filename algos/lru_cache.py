"""
Python implementation of LRU Cache

Two data structures are used to implement a LRU Cache

1. Doubly Linked List:
    The most recently used pages will be near front end and the least
    recently used pages will be near rear end

2. Dictionary:
    Key, Value pair. Value will correspond to the Queue
    node
"""


class Node:
    """
    Representation of a Node in a Doubly Linked List
    """

    def __init__(self, key, value, previous=None, next=None):
        """
        :param key: string
        :param value: string value
        :param previous: previous Node Object reference
        :param next: next Node Object reference
        """
        self.key = key
        self.value = value
        self.previous = previous
        self.next = next


class LRUCache:
    """
    Implementation for LRU Cache
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = None
        self.end = None

    def get(self, key):
        """
        Get the value in cache corresponding to a key.

        If key exists in the cache, then remove the corresponding
        Node from the Doubly Linked List and add it to the head of the list,
        making it the most recently used value

        If key does not exist in cache, throw a KeyError exception

        :param key: a hashable object(string, int, ...)
        :return: Node object
        """
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.set_head(node)
            return node

        raise KeyError("Key does not exist in cache")

    def remove(self, current_node):
        """
        Remove the current_node from its current location in the list
        and put it at the front
        :param current_node: Node object
        """

        if current_node.previous is not None:
            current_node.previous.next = current_node.next
        else:
            self.head = current_node.next

        if current_node.next is not None:
            current_node.next.previous = current_node.previous
        else:
            self.end = current_node.previous

        return

    def set_head(self, current_node):
        """
        Sets the given node as head in a Doubly Linked List
        :param current_node: Node object in Doubly Linked List
        """

        current_node.next = self.head
        current_node.previous = None

        if self.head is not None:
            self.head.previous = current_node

        self.head = current_node

        if self.end is None:
            self.end = self.head

    def insert(self, key, value):
        """
        If key exists in the cache, then update the value
        if necessary and move it to the front

        If key does not exist, then check for capacity. If capacity has
        exceeded, then evict the end node and insert the new node at the head
        :param key: a hashable object(string, int, ...)
        :param value: any object
        """
        if key in self.cache:
            old_node = self.cache[key]
            old_node.value = value
            self.remove(old_node)
            self.set_head(old_node)

        else:
            new_node = Node(key, value)

            if len(self.cache) >= self.capacity:
                self.remove(self.end)

            self.set_head(new_node)
            self.cache[key] = new_node

        return

    def print_cache(self):
        """
        Print the contents inside the cache in order
        Most Recent to Least recent
        """
        print "\n\nPrinting cache...(Most recent to least recent)\n"

        if self.head is None:
            print "Cache is empty"

        node = self.head

        while node is not None:
            print "Key = %s, Value = %s" % (node.key, node.value)
            node = node.next


if __name__ == '__main__':

    # Initialize Cache
    lru = LRUCache(5)
    lru.print_cache()

    for key, value in zip([10, 20, 30, 40, 50], ["ten", "twenty", "thirty", "forty", "fifty"]):
        lru.insert(key, value)

    lru.print_cache()

    # Cache is full, add something
    lru.insert(90, "ninety")
    lru.print_cache()

    # Add a value multiple times
    lru.insert(100, "hundred")
    lru.insert(100, "hundred")
    lru.insert(100, "hundred")
    lru.print_cache()


