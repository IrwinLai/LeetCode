# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def removeLeafNodes(self, root: TreeNode, t: int) -> TreeNode:
        def dfs(root):
            if root:
                if root.left:
                    root.left = dfs(root.left)
                if root.right:
                    root.right = dfs(root.right)
                if root.val == t and not root.left and not root.right:
                    root = None
                    return root
            return root
        root = dfs(root)
        return root
        