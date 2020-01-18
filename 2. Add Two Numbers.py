# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        
        #'''
        carry = 0
        ret = temnode = ListNode(0)
        while l1 or l2 or carry:
            tem = 0
            if l1:
                tem += l1.val
                l1 = l1.next
            if l2:
                tem += l2.val
                l2 = l2.next
            tem += carry
            carry = tem // 10
            temnode.next = ListNode(tem % 10)
            temnode = temnode.next
        
        return ret.next
        #'''