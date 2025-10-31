# https://leetcode.com/problems/subtree-of-another-tree/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p and not q:
                return True
            elif not p and q:
                return False
            elif not q and p:
                return False
            else:
                return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

        def dfs(node):
            if not node:
                return False

            res = False
            if node.val == subRoot.val:
                res = isSameTree(node, subRoot)

            if not res:
                res = dfs(node.left) or dfs(node.right)
            return res

        return dfs(root)
