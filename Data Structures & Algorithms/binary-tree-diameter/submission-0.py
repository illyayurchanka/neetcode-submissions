# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    diameter = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.get_length(root)
        return self.diameter
    def get_length(self, root) -> int:
        if root is None:
            return 0
        ll = self.get_length(root.left)
        lr = self.get_length(root.right)
        self.diameter = max(ll + lr, self.diameter)
        return max(ll, lr) + 1