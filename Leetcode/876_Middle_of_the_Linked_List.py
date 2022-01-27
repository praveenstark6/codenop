"""
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

problem link:
https://leetcode.com/problems/middle-of-the-linked-list/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            # slow 1x  1 2 3 4
            # fast 2x  1 3 5 7
            slow, fast = head, head

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow
