# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')

        def dfs(root):
            if not root:
                return 0

            nonlocal res
            # If the sum of left is negative, replace it with 0 to ignore that branch.
            left = max(0, dfs(root.left))
            right = max(0, dfs(root.right))

            # We try making this current node as root (include left and right)
            split = root.val + left + right
            res = max(res, split)

            # But we still update the largest path to the parent.
            return max(root.val + left, root.val + right)

        # We don't care about the return value as the max value is stored in res.
        dfs(root)
        return res