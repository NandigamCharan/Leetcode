# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def recurse(p):
            if p == None:
                return
            p.right, p.left = p.left, p.right
            recurse(p.left)
            recurse(p.right)
        
        recurse(root)
        return root