# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def sum_node(node: Optional[ListNode]) -> int:
            num = 0
            coeff = 1
            while node:
                num += node.val * coeff
                coeff *= 10
                node = node.next
            return num
        num1 = sum_node(l1)
        num2 = sum_node(l2)

        def get_list(num):
            head = ListNode()
            node = head
            prev = None
            if num == 0:
                head.val = 0
                return head
            while num != 0:
                node.val = num % 10
                num = num // 10
                node.next = ListNode()
                prev = node
                node = node.next
            prev.next = None
            return head

        return get_list(num1 + num2)