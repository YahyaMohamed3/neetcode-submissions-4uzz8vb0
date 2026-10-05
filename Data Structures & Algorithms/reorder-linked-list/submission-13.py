class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None

        # reverse the second half

        cur = second
        prev = None

        while cur:
            next_n = cur.next
            cur.next = prev
            prev = cur
            cur = next_n
        
        # merge while alternating starting from the first linked list
        second = prev
        first = head
        while second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2
