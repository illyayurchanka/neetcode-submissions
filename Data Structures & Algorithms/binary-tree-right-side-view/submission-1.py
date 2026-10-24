# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        stack = []
        curr_height = 0
        node = root
        height = 0
        while node:
            curr_height += 1
            if curr_height > height:
                height += 1
                ans.append(node.val)
            if node.right:
                if node.left:
                    stack.append([node.left, curr_height])
                node = node.right
            elif node.left:
                node = node.left
            elif stack:
                    node, curr_height = stack.pop()
            else:
                break
        
        return ans