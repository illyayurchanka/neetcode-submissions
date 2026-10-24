# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    count = 0
    def checkNode(self, root, curr_max):
        if root is None:
            return
        if root.val >= curr_max:
            curr_max = root.val
            self.count += 1
        self.checkNode(root.left, curr_max)
        self.checkNode(root.right, curr_max)
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return False
        self.checkNode(root, root.val)
        return self.count
        