# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invertNode(root):
            if root is None:
                return None
            if root.left:
                right = invertNode(root.left)
            else:
                right = None
            
            if root.right:
                left = invertNode(root.right)
            else:
                left = None
            return TreeNode(val=root.val, left=left, right=right)

        return invertNode(root)