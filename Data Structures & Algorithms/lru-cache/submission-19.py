class Node:
    def __init__(self, key, val):
        self.val, self.key = val, key
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity

        # {key: node}
        self.cache = {}
        # init left and right dummy nodes
        self.left, self.right = Node(0 , 0) , Node(0, 0)
        # doubly linked list left <-> right
        self.left.next , self.right.prev = self.right, self.left 

    # rewire pointers to drop given node to remove 
    # before: prev <-> node <-> next
    # after: prev <-> next
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev 

    # need to insert on the right side since we track LRU and MRU
    # MRU (right side), LRU (left side)
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        # insert node
        prev.next = nxt.prev = node
        # wire up new node 
        node.next , node.prev = nxt, prev 


    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1 

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        

