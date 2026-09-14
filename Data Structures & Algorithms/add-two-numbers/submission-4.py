# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        c1,c2 = l1, l2
        cur = dummy = ListNode(0)
        remainder = 0
        while c1 or c2 or remainder:
            v1 = c1.val if c1 else 0
            v2 = c2.val if c2 else 0

            val = v1 + v2
            val = val + remainder

            remainder = val//10

            cur.next = ListNode(val%10)
            cur = cur.next
            
            c1 = c1.next if c1 else None
            c2 = c2.next if c2 else None
        
        return dummy.next
            