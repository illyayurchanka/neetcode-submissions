"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        corr_arr = {None: None}

        node = head
        while node:
            corr_arr[node] = Node(x = node.val)
            node = node.next
        
        node = head
        while node:
            corr_arr[node].next = corr_arr[node.next]
            corr_arr[node].random = corr_arr[node.random]
            node = node.next
        
        return corr_arr[head] 