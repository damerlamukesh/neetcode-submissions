# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        res=[]
        queue=deque([root])
        while len(queue) != 0:
            level_height=len(queue)
            level=[]
            for i in range(level_height):
                e=queue.popleft()
                level.append(e.val)
                if e.left is not None:
                    queue.append(e.left)
                if e.right is not None:
                    queue.append(e.right)
            res.append(level)
        return res
        