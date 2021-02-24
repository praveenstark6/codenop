# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        H = set(G)
        
        count = 0         # 1  4- 2
        connected = False # True 3- False
        
        while head:
            if head.val in H and not connected:
                connected = True
                count += 1
            elif head.val not in G and connected:
                connected = False
            
            head = head.next
            
        return count
        
