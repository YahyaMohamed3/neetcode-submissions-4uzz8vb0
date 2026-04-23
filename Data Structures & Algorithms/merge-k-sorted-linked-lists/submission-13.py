class ListNode:
    def __init__(self, val=0 , next=None):
        self.val = val
        self.next = next

class NodeWrapper:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val



class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if  len(lists) == 0:
            return None
        
        min_heap = []
        res = ListNode(0)
        cur = res

        for lst in lists:
            if lst is not None:
                heapq.heappush(min_heap, NodeWrapper(lst))
        
        while min_heap:
            nodeWrapper = heapq.heappop(min_heap)
            cur.next = nodeWrapper.node
            cur = cur.next

            if nodeWrapper.node.next:
                heapq.heappush(min_heap, NodeWrapper(nodeWrapper.node.next))
        return res.next

