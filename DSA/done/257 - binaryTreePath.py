# https://leetcode.com/problems/binary-tree-paths/

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        cur = []

        def backTrack(node):
            nonlocal cur
            if not node:
                return 
            if not node.left and not node.right:
                cur.append(str(node.val))
                tmp = "".join(cur)
                res.append(tmp)
                cur.pop()
                return 

            cur.append(str(node.val))
            cur.append("->")
            backTrack(node.left)
            backTrack(node.right)
            cur.pop()
            cur.pop()

        backTrack(root)
        return res