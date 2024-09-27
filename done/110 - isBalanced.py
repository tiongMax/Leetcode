# https://leetcode.com/problems/balanced-binary-tree/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return (0, True)

            h1, b1 = dfs(node.left)
            h2, b2 = dfs(node.right)
            cur_height = 1 + max(h1, h2)
            if b1 and b2 and abs(h1 - h2) <= 1:
                return (cur_height, True)
            else:
                return (cur_height, False)

        return dfs(root)[1]