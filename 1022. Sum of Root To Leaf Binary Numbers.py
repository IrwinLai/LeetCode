# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        
        def dfs(root, s = 0) -> int:
            if root is None:
                 return 0
            s = s*2 + root.val
            if root.left == root.right: # null
                return s
            else:
                return dfs(root.left, s) + dfs(root.right, s)
        
        s = dfs(root, 0)
        
        return s
            