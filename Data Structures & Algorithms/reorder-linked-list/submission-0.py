# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None or head.next is None:
            return
        length = 1
        node = head.next
        while node is not None:
            node = node.next
            length += 1

        print(length)
        def get_before_the_last_node():
            node = head
            for _ in range(length - 2):
                node = node.next
            return node

        prev_node = head

        for i in range((length - 1) // 2):
            before_the_last = get_before_the_last_node()
            before_the_last.next.next = prev_node.next
            prev_node.next = before_the_last.next
            before_the_last.next = None
            prev_node = prev_node.next.next


     
       