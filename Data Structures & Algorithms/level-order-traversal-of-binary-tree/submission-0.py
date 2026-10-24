# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        lst = [[root]]
        while lst[-1][0] is not None:
            level = []
            for l in lst[-1]:
                if l.left is not None:
                    level.append(l.left)
                if l.right is not None:
                    level.append(l.right)
            if len(level) == 0:
                break
            lst.append(level)
        v_lst = []
        for l in lst:
            level = []
            if l[0] is None:
                break
            for node in l:
                    level.append(node.val)
            v_lst.append(level)
        return v_lst