# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def dfs(root,p,gp):
            if root:
                if gp == 0: # grandparent is even
                    gp = p
                    p = root.val % 2
                    return dfs(root.left,p,gp) + dfs(root.right,p,gp) + root.val
                else:
                    gp = p
                    p = root.val % 2
                    return dfs(root.left,p,gp) + dfs(root.right,p,gp)
            else:
                return 0
        return dfs(root,1,1)
                