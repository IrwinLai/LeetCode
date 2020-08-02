# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        def dfs(root):
            if root:
                root.l = []
                root.r = []
                # is leave
                if not root.left and not root.right:
                    return [0]
                
                else:
                    teml,temr = [],[]
                    if root.left:
                        teml = dfs(root.left)
                        for i in range(len(teml)):
                            teml[i] += 1
                        root.l = teml
                        
                    if root.right:
                        temr = dfs(root.right)
                        for i in range(len(temr)):
                            temr[i] += 1
                        root.r = temr
                    
                    return teml + temr
        
        
        ans = [0]
        def check(root):
            if root:
                for i in root.l:
                    for j in root.r:
                        if i+j <= distance:
                            ans[0] += 1
                check(root.left)
                check(root.right)
        
        dfs(root)
        check(root)
        
        return ans[0]