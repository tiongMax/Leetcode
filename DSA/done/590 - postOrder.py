# https://leetcode.com/problems/n-ary-tree-postorder-traversal/
from typing import List

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        elif not root.children:
            return [root.val]

        res = []
        def dfs(node):
            if not node:
                return

            for n in node.children:
                dfs(n)
            res.append(node.val)

        dfs(root)
        return res
