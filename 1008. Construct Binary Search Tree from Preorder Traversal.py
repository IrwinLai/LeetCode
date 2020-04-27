# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, p: List[int]) -> TreeNode:
        if not p:
            return None
        else:
            root = TreeNode(p[0])
            index = bisect.bisect_right(p,p[0])
            root.left = self.bstFromPreorder(p[1:index])
            root.right = self.bstFromPreorder(p[index:])
        return root