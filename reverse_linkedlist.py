# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return 
        rev = None
        while head:
            n = head.next
            head.next = rev
            rev = head
            head = n
        return rev
