# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if root==None:
                return True
            LHS=dfs(root.left)
            if LHS==-1:
                return -1
            RHS=dfs(root.right)
            if RHS==-1:
                return -1
            if abs(LHS-RHS)>1:
                return -1
            return 1+max(LHS,RHS)

        s=dfs(root)
        if s==-1:
            return False
        return True
        