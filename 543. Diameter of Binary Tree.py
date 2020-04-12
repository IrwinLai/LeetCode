# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 0
        def helper(root):
            if root:
                left,right = helper(root.left),helper(root.right)
                self.ans = max(self.ans,left+right)
                return max(left,right)+1
            return 0
        helper(root)
        
        return self.ans