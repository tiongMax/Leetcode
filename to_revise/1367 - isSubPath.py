# https://leetcode.com/problems/linked-list-in-binary-tree/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def dfs(head, root):
            if not head:
                return True
            elif not root or (head.val != root.val):
                return False

            left = dfs(head.next, root.left)
            right = dfs(head.next, root.right)
            return left or right

        if dfs(head, root):
            return True
        elif not root:
            return False
        else:
            left = self.isSubPath(head, root.left) 
            right = self.isSubPath(head, root.right)
            return left or right