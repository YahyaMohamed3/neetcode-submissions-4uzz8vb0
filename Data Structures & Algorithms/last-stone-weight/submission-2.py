import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            stone1 , stone2 = heapq.heappop(heap), heapq.heappop(heap)
            res = stone1 - stone2
            if res < 0:
                heapq.heappush(heap, res)
        return -heap[0] if heap else 0

