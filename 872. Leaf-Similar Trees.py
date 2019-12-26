# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def dfs(root):
            if root is None:
                return []
            if root.left == root.right:
                return [root.val]
            else:
                return dfs(root.left) + dfs(root.right)
        return dfs(root1) == dfs(root2)