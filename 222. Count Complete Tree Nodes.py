# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        self.size = 0
        
        def helper(root):
            if root:
                self.size += 1
            if root.left:
                helper(root.left)
            if root.right:
                helper(root.right)
                
        if root: helper(root)
        return self.size