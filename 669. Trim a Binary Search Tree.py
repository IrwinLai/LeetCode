# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        def trim(root,L,R):
            if root:
                if root.val > R:
                    return trim(root.left,L,R)
                elif root.val < L:
                    return trim(root.right,L,R)
                else:
                    root.left = trim(root.left,L,R)
                    root.right = trim(root.right,L,R)
                    return root
        return trim(root,L,R)