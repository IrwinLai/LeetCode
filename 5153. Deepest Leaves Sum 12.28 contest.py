# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        def dfs(root,d,depth):
            if root is None:
                return d
            depth += 1
            d = dfs(root.left,d,depth)
            d = dfs(root.right,d,depth)
            d[depth] = d.get(depth,0) + root.val
            return d
            
        d = {}
        depth = 0
        dfs(root,d,depth)
        return d[max(list(d.keys()))]