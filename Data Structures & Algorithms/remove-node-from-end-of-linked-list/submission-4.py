# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        node = head
        while node:
            node = node.next
            length += 1
        if length == 1:
            head = None
            return head
        
        prev_node = None 
        node = head
        for _ in range(length - n):
            prev_node = node
            node = node.next
        if prev_node is None:
            return node.next
        prev_node.next = node.next
        return head
