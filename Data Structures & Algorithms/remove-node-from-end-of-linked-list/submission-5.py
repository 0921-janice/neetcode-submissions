# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        cur = head

        while cur:
            length += 1
            cur = cur.next 

        cur, prev = head, None

        for _ in range(length - n):
            prev = cur
            cur = cur.next

        if prev == None:
            return head.next
            
        prev.next = cur.next

        return head






        



















        l1 = l2 = head

        for i in range(n):
            l2 = l2.next

        if not l2:
            return head.next
        
        while l2.next:
            l1 = l1.next
            l2 = l2.next
        
        l1.next = l1.next.next

        return head

