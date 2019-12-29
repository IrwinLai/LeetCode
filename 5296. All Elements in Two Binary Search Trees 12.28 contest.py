# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def dfs(root):
            ret = []
            if root is None:
                return []
            ret = dfs(root.left) + dfs(root.right)
            ret.append(root.val)
            return ret
        return sorted(dfs(root1) + dfs(root2))
            