"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ret = []
        if root is None:
            return []
        for i in range(len(root.children)):
                ret.extend(self.postorder(root.children[i]))
        ret.append(root.val)
        return ret