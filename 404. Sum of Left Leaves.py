# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def dfs(root):
            if not root:
                return 0
            tem = 0
            if root.left:
                if not root.left.left and not root.left.right:
                    tem = tem + root.left.val + dfs(root.left)
                else:
                    tem += dfs(root.left)
            if root.right:
                tem += dfs(root.right)
            return tem
        
        return dfs(root)
                