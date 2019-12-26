# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def invert(root):
            if root is None:
                return 0
            invert(root.left)
            invert(root.right)
            root.left,root.right  = root.right,root.left
        invert(root)
        return root