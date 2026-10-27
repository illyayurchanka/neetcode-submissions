# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(root, lbound, rbound) -> bool:
            if root is None:
                return True
            if not (lbound < root.val < rbound):
                return False
            return valid(root.right, root.val, rbound) and valid(root.left, lbound, root.val)
        return valid(root, -math.inf, math.inf)