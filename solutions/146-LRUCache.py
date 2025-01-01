'''
Time Complexity: O(1)
Space Complexity: O(capacity)
'''

# define doubly linked list node
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

# define doubly linked list
class DoublyLinkedList:
    def __init__(self):
        # dummy head & tail to simplify insertion/removal and avoid edge cases
        self.head = Node(0, 0) 
        self.tail = Node(0, 0) 
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_to_head(self, node):
        # add node right after head
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def remove_node(self, node):
        # remove existing node from DLL
        node.prev.next = node.next
        node.next.prev = node.prev

    def remove_tail(self):
        # remove node before the tail (LRU)
        if self.tail.prev == self.head:
            return None # DLL is empty
        lru_node = self.tail.prev
        self.remove_node(lru_node)
        return lru_node

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.list = DoublyLinkedList()
        self.cache = {} # maps keys to nodes

    def get(self, key):
        # move accessed node to head or return -1
        if key in self.cache:
            node = self.cache[key]
            self.list.remove_node(node)
            self.list.add_to_head(node)
            return node.value
        return -1

    def put(self, key, value):
        if key in self.cache:
            # update value and move to head
            node = self.cache[key]
            node.value = value
            self.list.remove_node(node)
            self.list.add_to_head(node)
        else:
            if len(self.cache) >= self.capacity: 
                lru_node = self.list.remove_tail()
                del self.cache[lru_node.key]
            new_node = Node(key, value)
            self.cache[key] = new_node
            self.list.add_to_head(new_node)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)