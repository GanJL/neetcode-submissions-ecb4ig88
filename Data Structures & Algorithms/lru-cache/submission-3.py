class Node():
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.left = Node(0,0)
        self.right = Node(0,0)

        self.left.next = self.right
        self.right.prev = self.left
    
    # cache hashmap function
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            self.cache[node.key] = node
            return node.value
        return -1

    # cache hashmap function
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        node = Node(key, value)
        self.insert(node)
        self.cache[key] = node

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
            
    # list function - manipulate linked list by linking
    def insert(self, node):
        lru, mru = self.left.next, self.right.prev
        mru.next = node #new mru
        self.right.prev = node
        node.next = self.right
        node.prev = mru
    # list function - manipulate linked list by unlinking
    def remove(self, node):
        node_prev, node_next = node.prev, node.next
        node_prev.next, node_next.prev = node_next, node_prev
