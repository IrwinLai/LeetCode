# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        def helper(head,root):
            if not head:
                return True
            if not root:
                return False
            return head.val == root.val and (helper(head.next, root.left) or helper(head.next, root.right))
        if not head:
            return True
        if not root:
            return False
        return helper(head,root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)