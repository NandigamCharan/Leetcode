# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.A = []
        self.current = 0
        self.len = 0
        self.inorder(root)

    def inorder(self, node):
        if node == None:
            return
        self.inorder(node.left)
        self.A.append(node.val)
        self.len += 1
        self.inorder(node.right)
            

    def next(self) -> int:
        self.current += 1
        return self.A[self.current - 1]

    def hasNext(self) -> bool:
        if self.current < self.len:
            return True
        else:
            return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()