# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        f,s = head, head

        # fast and slow pointer to find middle of LL
        while f.next and f.next.next:
            f = f.next.next
            s = s.next

        second = s.next
        prev = s.next = None

        #reverse second half
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        #merge two LL
        first, second = head, prev

        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first =  temp1
            second = temp2


        