"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def dfs(root):
            ret = 0
            if root is None:
                return 0
            for child in root.children:
                ret = max(dfs(child),ret)
            return ret+1   # plus one here, not in for loop
        
        return dfs(root)
        