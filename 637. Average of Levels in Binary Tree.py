# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        ret = []
        i = 0
        s = [root]
        while(len(s) > 0):
            count = 0
            ret.append(0)
            n = len(s)
            for j in range(n):
                if s[0]:
                    ret[i] += s[0].val
                    count += 1
                    if s[0].left:
                        s.append(s[0].left)
                    if s[0].right:
                        s.append(s[0].right)
                s.pop(0)
            ret[i] /= count
            i += 1
        return ret