# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def maxLength(root, count):
            if root:
                count += 1
            else:
                return count
            if root.left:
                lcount = maxLength(root.left, count)
            else:
                lcount = count
            if root.right:
                rcount = maxLength(root.right, count)
            else:
                rcount = count
            return max(lcount, rcount)
        return maxLength(root, 0)