import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hashmap = {}
        for task in tasks:
            hashmap[task] = hashmap.get(task, 0) + 1
        heap = [-c for c in hashmap.values()]
    
        heapq.heapify(heap)
        time = 0
        q = deque()

        while q or heap:
            time += 1
            if heap:
                count = heapq.heappop(heap) + 1
                if count != 0:
                    q.append((count, time + n))
            if q and q[0][1] == time:
                heapq.heappush(heap ,q.popleft()[0])
        return time

                
        
