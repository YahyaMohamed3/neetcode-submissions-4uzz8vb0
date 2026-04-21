from collections import deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hashMap = {}
        heap = []
        for task in tasks:
            hashMap[task] = hashMap.get(task, 0) + 1
        heap = [-c for c in hashMap.values()]

        heapq.heapify(heap)
        time = 0
        queue = deque()

        while heap or queue:
            time += 1
            if heap:
                count = heapq.heappop(heap) + 1
                if count != 0:
                    queue.append((count, time + n))
            if queue and queue[0][1] == time:
                heapq.heappush(heap, queue.popleft()[0])
        return time 