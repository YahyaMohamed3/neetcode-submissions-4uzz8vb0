from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        # order dict keep track of most recently used unlike dict {}
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        # pop from front we always push MRU to end 
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
        

        


