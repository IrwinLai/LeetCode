# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        def dfs1(root):
            if not root:
                return 0
            else:
                root.val += dfs1(root.left) + dfs1(root.right)
            return root.val
        
        def dfs2(root,m):
            t1,t2 = 0,0
            if root.left:
                t1 = max((m-root.left.val)*root.left.val,dfs2(root.left,m))
            if root.right:
                t2 = max((m-root.right.val)*root.right.val,dfs2(root.right,m))
            return max(t1,t2)
        
        dfs1(root)
        return (dfs2(root,root.val))%(10**9 + 7)
            
        
        