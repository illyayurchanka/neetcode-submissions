# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node1, node2 = list1, list2

        if node1 is None: return node2
        if node2 is None: return node1
        
        if node1.val < node2.val:
            new_list = ListNode(val = node1.val)
            node1 = node1.next
        else:
            new_list = ListNode(val = node2.val)
            node2 = node2.next
        res = new_list
        while (node1 is not None) and (node2 is not None):
            if node1.val < node2.val:
                new_list.next = ListNode(val = node1.val)
                node1 = node1.next
                new_list = new_list.next
            else:
                new_list.next = ListNode(val = node2.val)
                node2 = node2.next
                new_list = new_list.next

        while node1 is not None:
                new_list.next = ListNode(val = node1.val)
                node1 = node1.next
                new_list = new_list.next

        while node2 is not None:
                new_list.next = ListNode(val = node2.val)
                node2 = node2.next
                new_list = new_list.next

        return res 
