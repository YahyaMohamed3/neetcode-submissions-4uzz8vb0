class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        
        slow = fast = head
        # need to find the midpoint and chop off the second part

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None


        # reverse the chopped off part
        cur = second
        prev = None

        while cur:
            next_n = cur.next
            cur.next = prev
            prev = cur
            cur = next_n
        
        second = prev
        first = head

        # merge while alternating starting from the first list

        while second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2
        
        

