# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        
        def dfs(start,end):
            if start == end:
                return None
            ret = []
            for i in range(start,end):
                for l in dfs(start,i) or [None]:
                    for r in dfs(i+1,end) or [None]:
                        node = TreeNode(i)
                        node.left = l
                        node.right = r
                        ret.append(node)
            return ret
        
        if n == 0:
            return []
        return dfs(1,n+1)