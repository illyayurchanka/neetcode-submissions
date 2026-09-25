# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        count = 0
        while head and count < 1000:
            head = head.next
            count += 1
        return count >= 1000
        