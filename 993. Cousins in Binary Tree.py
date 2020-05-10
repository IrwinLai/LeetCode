# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        #bfs
        flag = 0
        search = [(root,root)]
        while search:
            tem = []
            for i in search:
                if i[0].left:
                    tem.append((i[0].left,i[0]))
                if i[0].right:
                    tem.append((i[0].right,i[0]))
            search = tem
            for i in search:
                print(0, i[0].val)
                if i[0].val == x or i[0].val == y:
                    # find first
                    if flag == 0:
                        flag = 1
                        parent = i[1]
                    elif flag == 1:
                        if parent != i[1]:
                            return True
                        else:
                            return False
            if flag == 1:
                return False
        return False
        