# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxx=float("-inf")
        def maxxi(root):
           
            if root == None:
                return 0
            lhs=maxxi(root.left)
            if lhs<0:
                lhs=0
            rhs=maxxi(root.right)
            if rhs <0:
                rhs=0
            self.maxx=max(self.maxx,lhs+rhs+root.val)
            return root.val + max(lhs,rhs)
        
        maxxi(root)
        return self.maxx
        