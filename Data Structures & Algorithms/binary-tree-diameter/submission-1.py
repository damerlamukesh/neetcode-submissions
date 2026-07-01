# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dia=0
        def dfs(root):
            if root==None:
                return 0
            LHS=dfs(root.left)
            RHS=dfs(root.right)
            self.dia=max(self.dia,LHS+RHS)
            return 1+max(LHS,RHS)
        dfs(root)
        return self.dia
        