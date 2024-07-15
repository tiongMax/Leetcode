# https://leetcode.com/problems/create-binary-tree-from-descriptions/

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Mine
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        hm = {}

        for p, c, l in descriptions:
            if c in hm:
                hm[c][1] = p
                child = hm[c][0]
            else:
                child = TreeNode(c)
                hm[c] = [child, p]

            if p not in hm:
                hm[p] = [TreeNode(p), -1]

            if l:
                hm[p][0].left = child
            else:
                hm[p][0].right = child

        for v, p in hm.values():
            if p == -1:
                return v

# Neetcode's
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        hm = {}
        child_set = set()
        
        for p, c, l in descriptions:
            if p not in hm:
                hm[p] = TreeNode(p)
            if c not in hm:
                hm[c] = TreeNode(c)
                
            child_set.add(c)
            
            if l == 1:
                hm[p].left = hm[c]
            else:
                hm[p].right = hm[c]

        # Find the root (which is not a child of any node)
        for p, node in hm.items():
            if p not in child_set:
                return node
