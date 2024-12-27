# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Approach 1
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = []
        res = dummy = TreeNode()
        while stack or root:
            if root:
                dummy.right = root
                dummy = dummy.right
                temp = dummy.left
                dummy.left = None
                if root.right:
                    stack.append(root.right)
                root = temp
            else:
                root = stack.pop()

        root = res.right

# Approach 2 
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        # Use a stack to keep track of nodes
        stack = [root]

        # Previous node in the flattened tree
        prev = None

        while stack:
            node = stack.pop()

            if prev:
                prev.right = node
                prev.left = None

            left = node.left
            right = node.right

            # First push right child to stack, because we want to process left child first
            if right:
                stack.append(right)
            if left:
                stack.append(left)

            # Move prev pointer to current node
            prev = node


        