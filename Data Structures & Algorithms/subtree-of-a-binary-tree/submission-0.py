# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def are_equal(root, subRoot):
            if subRoot is None and root is None:
                return True 
            elif subRoot is None:
                return False 
            elif root is None:
                return False 
            print(root.val)
            if root.val == subRoot.val:
                return are_equal(root.left, subRoot.left) and are_equal(root.right, subRoot.right)
            return False
        def tsearch(root, subRoot) -> bool:
            if root is None:
                return False
            print(root.val)
            if root.val == subRoot.val:
                check = are_equal(root, subRoot)
                if check:
                    return True
            return tsearch(root.left, subRoot) or tsearch(root.right, subRoot)
        return tsearch(root, subRoot)