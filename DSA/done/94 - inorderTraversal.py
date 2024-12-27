# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Approach 1: Iterative
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        # Go all the way to left and add them to the stack at the same time.
        # If left is null, pop and do something, then continue to the right.
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                res.append(root.val)
                root = root.right

        return res

# Approach 2: Recursive
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        lis = []

        def traverse(root, lis):
            if not root:
                return lis
            
            traverse(root.left, lis)
            lis.append(root.val)
            traverse(root.right, lis)
            return lis
            
        return traverse(root, lis)