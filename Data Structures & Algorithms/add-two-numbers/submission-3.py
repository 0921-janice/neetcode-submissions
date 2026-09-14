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
        while c1 and c2:
            val = c1.val + c2.val
            val = val + remainder
            remainder = 0
            if val >= 10:
                remainder = val//10
                val = val%10

            cur.next = ListNode(val)
            cur = cur.next
            
            c1, c2 = c1.next, c2.next
        
        cur_pointer = c1 if c1 else c2

        while cur_pointer:
            val = cur_pointer.val + remainder
            remainder = 0

            if val >= 10:
                remainder = val//10
                val = val%10

            cur.next = ListNode(val)
            cur = cur.next
            
            cur_pointer = cur_pointer.next

        if remainder != 0:
            cur.next = ListNode(remainder)

        return dummy.next
            