# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        count = [0]
        
        def bfs(root,l):
            if root:
                if root.val in l:
                    l.remove(root.val)
                else:
                    l.append(root.val)
            if root.left:
                tem = l.copy()
                bfs(root.left,tem)
            if root.right:
                tem = l.copy()
                bfs(root.right,tem)
            if not root.left and not root.right:
                if len(l) <= 1:
                    count[0] += 1
        bfs(root,[])
        return count[0]
            