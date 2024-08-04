# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0 

        res = 0
        def rootToLeaf(root):
            if not root:
                return 0

            nonlocal res
            left = rootToLeaf(root.left)
            right = rootToLeaf(root.right)
            res = max(res, left + right) # Check the diameter on every node.

            return max(left, right) + 1

        rootToLeaf(root)
        return res 