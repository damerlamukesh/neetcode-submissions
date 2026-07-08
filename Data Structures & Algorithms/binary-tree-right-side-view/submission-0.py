# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        def rpo(node,level):
            if root==None:
                return None
            if len(ans)==level:
                ans.append(node.val)
            if node.right:
                rpo(node.right,level+1)
            if node.left:
                rpo(node.left,level+1)

        rpo(root,0) 
        return ans
        