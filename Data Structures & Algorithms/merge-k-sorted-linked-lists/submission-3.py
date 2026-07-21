# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def mergeTwoLists(l1,l2):
            dum = ListNode()
            cur = dum

            while l2 and l1:
                if l1.val <= l2.val:
                    cur.next = l1
                    l1 = l1.next
                
                else:
                    cur.next = l2
                    l2 = l2.next
                
                cur = cur.next

            cur.next = l1 if not l2 else l2

            return dum.next

        for i in range(1, len(lists)):
            lists[i] = mergeTwoLists(lists[i], lists[i-1])

        return lists[-1] if lists else None

     













