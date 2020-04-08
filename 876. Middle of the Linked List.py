# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
        
        
        '''
        l = []
        tem = head
        while tem:
            l.append(tem.val)
            tem = tem.next
        index = (len(l))//2
        while index > 0:
            index -= 1
            head = head.next
        return head
        '''