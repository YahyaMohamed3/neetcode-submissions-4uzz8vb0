# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #[1, 2, 3]
        # head = node(1, node(2))
        cur = head # cur = 1
        prev = None # prev = None
        while cur:
            next_node = cur.next #next_node = node(2)
            cur.next = prev # cur.next used to point to Node(2) now what does it point to None
            prev = cur   # cur = 1 prev = 1 [None <- Node(1) , Node(2) -> Node(3) -> none]
            cur = next_node
        return prev






