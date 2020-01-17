# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        dq = [(root,0)]
        width = [1]
        while len(dq):
            n = len(dq)
            for i in range(n):
                pos = dq[0][1]
                if dq[0][0].left:
                    dq.append((dq[0][0].left,pos*2))
                if dq[0][0].right:
                    dq.append((dq[0][0].right,pos*2+1))
                dq.pop(0)
            if len(dq):
                width.append(dq[-1][1] - dq[0][1] + 1)
        return max(width)
            