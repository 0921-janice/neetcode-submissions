# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head

        #find middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #reverse second half
        cur, prev = slow.next, None
        slow.next = None

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        #re order list

        l1,l2 = head, prev
        

        while l1 and l2:
            temp1 = l1.next
            temp2 = l2.next
            l1.next = l2
            l2.next = temp1
            l1 = temp1
            l2 = temp2













