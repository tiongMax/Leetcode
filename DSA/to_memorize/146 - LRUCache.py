# https://leetcode.com/problems/lru-cache/

class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lru = Node(-1, -1)  # Dummy LRU node
        self.mru = Node(-1, -1)  # Dummy MRU node
        self.lru.next = self.mru
        self.mru.prev = self.lru
        self.cache = {}  # Maps key to node

    def insert(self, node: Node) -> None:
        # Insert node right before MRU (most recently used)
        prev, next = self.mru.prev, self.mru
        prev.next = node
        node.prev = prev
        node.next = next
        next.prev = node

    def remove(self, node: Node) -> None:
        # Remove an existing node from the list
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev
        node.prev = node.next = None  # Clear references

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        # Move the accessed node to the MRU position
        node = self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update the value of the existing node and move it to the MRU position
            node = self.cache[key]
            node.value = value
            self.remove(node)
            self.insert(node)
        else:
            # Create a new node and insert it
            node = Node(key, value)
            self.cache[key] = node
            self.insert(node)
        
        if len(self.cache) > self.capacity:
            # Remove the LRU (least recently used) node
            lru_node = self.lru.next
            self.remove(lru_node)
            del self.cache[lru_node.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
