class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        

        # find mid 
        fast = slow = head 

        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next
        
        second = slow.next 
        slow.next = None


        cur = second 
        prev = None

        while cur:
            next_n = cur.next
            cur.next = prev
            prev = cur
            cur = next_n
        
        first = head
        second = prev

        while second:
            tmp1 , tmp2 = first.next, second.next
            first.next , second.next = second, tmp1
            first, second = tmp1, tmp2
        
        

