# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        dq = [root]
        ret = [[root.val]]
        p = 1
        c = 0
        while(len(dq) > 0):
            temlist = []
            sz = len(dq)
            for i in range(sz):
                if dq[0].left:
                    dq.append(dq[0].left)
                    temlist.append(dq[0].left.val)
                if dq[0].right:
                    dq.append(dq[0].right)
                    temlist.append(dq[0].right.val)
                dq.pop(0)
            if len(temlist) > 0 :
                ret.extend([temlist])
        return ret
            
                