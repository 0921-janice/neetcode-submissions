# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n == 0:
            return head

        dummy = ListNode(next = head)
        l,r = dummy, head

        while n != 0 and r:
            r = r.next
            n -= 1

        while r:           
            r = r.next
            l = l.next

        l.next = l.next.next if l.next.next else None

        return dummy.next