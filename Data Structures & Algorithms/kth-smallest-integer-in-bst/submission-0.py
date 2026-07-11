# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        self.count = self.val = 0
        
        def dfs(node):
            if not node or self.val != 0:
                return 
            
            

            dfs(node.left)
            self.count += 1

            if self.count == k:
                self.val = node.val
                return

            dfs(node.right)

        dfs(root)
        return self.val
        