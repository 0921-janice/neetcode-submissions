# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def sameTree(n1, n2):
            if not n1 and not n2:
                return True

            if not n1 or not n2 or n1.val != n2.val:
                return False

            return sameTree(n1.left, n2.left) and sameTree(n1.right, n2.right)

        if not root:
            return False

        if not subRoot:
            return True

        if sameTree(root, subRoot):
            return True


        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)























        # def sameTree(r1,r2):
        #     if not r1 and not r2:
        #         return True

        #     if not r1 or not r2:
        #         return False

        #     if not r1.val == r2.val:
        #         return False

        #     return sameTree(r1.left, r2.left) and sameTree(r1.right, r2.right)

        # if not root:
        #     return False
        
        # if not subRoot:
        #     return True

        # if sameTree(root, subRoot):
        #     return True

        # return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)




















        

        

        