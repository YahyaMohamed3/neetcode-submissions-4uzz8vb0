class Node:
    def __init__(self, key=0, value=0, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.hashMap = {} #{key: Node}
        self.left , self.right = Node(), Node()
        self.left.next = self.right
        self.right.prev = self.left
    
    def add(self, node):
        rightPrev = self.right.prev

        node.next = self.right
        node.prev = rightPrev
        self.right.prev = node
        rightPrev.next = node
    
    def remove(self, node):
        nodePrev, nodeNext = node.prev, node.next
        nodePrev.next = nodeNext
        nodeNext.prev = nodePrev
    
    def get(self, key):
        if key in self.hashMap:
            node = self.hashMap[key]
            self.remove(node)
            self.add(node)
            return node.value
        else:
            return -1
    
    def put(self, key, value):
        if key in self.hashMap:
            node = self.hashMap[key]
            node.value = value
            self.remove(node)
            self.add(node)
            return
        
        node = Node(key, value)
        self.hashMap[key] = node
        self.add(node)

        if len(self.hashMap) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.hashMap[lru.key]

