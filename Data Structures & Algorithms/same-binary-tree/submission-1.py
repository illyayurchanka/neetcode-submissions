# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        are_same = ((p is not None) == (q is not None))
        if p is None or q is None:
            return are_same
        are_same &= (p.val == q.val)
        are_same &= self.isSameTree(p.right, q.right)
        are_same &= self.isSameTree(p.left, q.left)
        return are_same 