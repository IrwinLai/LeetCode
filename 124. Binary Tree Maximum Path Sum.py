# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max = float('-inf')
        def bfs(node):
            if node:
                l = max(bfs(node.left),0)
                r = max(bfs(node.right),0)
                self.max = max(self.max, l+r+node.val)
                return max(l,r,0)+node.val
            else:
                return 0
        bfs(root)
        return self.max