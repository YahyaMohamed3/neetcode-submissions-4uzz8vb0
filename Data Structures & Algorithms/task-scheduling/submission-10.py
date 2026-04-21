from collections import deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hashmap = {}
        for task in tasks:
            hashmap[task] = hashmap.get(task, 0) + 1   
        heap = [-c for c in hashmap.values()]
        heapq.heapify(heap)
        q = deque()
        time = 0 

        while heap or q:
            time += 1
            if heap:
                count = heapq.heappop(heap) + 1
                if count != 0:
                    q.append((count, n + time))
            if q and q[0][1] == time:
                heapq.heappush(heap , q.popleft()[0])
        return time 

