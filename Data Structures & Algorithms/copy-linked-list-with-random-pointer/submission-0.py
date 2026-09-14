"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_new = {}
        dummy = Node(-1)
        old_cur, new_cur = head, dummy

        while old_cur:
            new_cur.next = Node(old_cur.val)
            new_cur = new_cur.next 
            old_to_new[old_cur] = new_cur
            old_cur = old_cur.next

        old_cur, new_cur = head, dummy.next

        while old_cur:
            random = old_cur.random
            new_cur.random = old_to_new[random] if random != None else None
            new_cur = new_cur.next 
            old_cur = old_cur.next

        return dummy.next