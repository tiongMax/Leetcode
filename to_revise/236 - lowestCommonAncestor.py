# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Time: O(n), space: O(1)
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        elif left:
            return left
        else:
            return right
        
# Time: O(n), space: O(n)
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def rootToTarget(node, t, visited):
            if not node:
                return False

            visited.append(node.val)
            if node.val == t.val:
                return True

            if rootToTarget(node.left, t, visited) \
                or rootToTarget(node.right, t, visited):
                return True
            
            visited.pop()
            return False

        s1 = []
        s2 = []
        rootToTarget(root, p, s1)
        rootToTarget(root, q, s2)
        
        i = j = 0
        node = None
        while i < len(s1) and j < len(s2):
            if s1[i] == s2[j]:
                node = s1[i]
                i += 1
                j += 1
            else:
                break
        
        return TreeNode(node)



            
        
        