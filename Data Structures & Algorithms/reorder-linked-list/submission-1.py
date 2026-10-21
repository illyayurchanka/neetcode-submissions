# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None or head.next is None:
            return
        fast_node = head.next.next
        slow_node = head.next
        mid_node = None


        while fast_node and fast_node.next is not None:
            slow_node = slow_node.next
            fast_node = fast_node.next.next

        second = slow_node.next
        slow_node.next = None
        prev = None

        while second:
            second.next, prev, second = prev, second, second.next

        first, second = head, prev

        while second:
            first.next, first = second, first.next
            second.next, second = first, second.next
            


     
       