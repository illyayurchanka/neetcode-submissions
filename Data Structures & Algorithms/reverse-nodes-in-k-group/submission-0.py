# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def rev_list(head, k):
            prev = None
            curr = head
            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            head.next = curr
            return prev
        
        def check_len(node, k):
            for _ in range(k):
                if node is None:
                    return False
                node = node.next
            return True
        
        if not check_len(head, k):
            return head
        
        return_head = rev_list(head, k)
        prev_tail = head
        node = head.next
        while check_len(node, k):
            new_head = rev_list(node, k)
            prev_tail.next = new_head
            prev_tail = node
            node = node.next
        
        return return_head

            
            
