# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Approach 1: Recursive
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        self.traverse(root, stack)
        return stack

    def traverse(self, node, stack):
        if not node:
            return stack
        
        stack.append(node.val)
        self.traverse(node.left, stack)
        self.traverse(node.right, stack)
        return stack
    
# Approach 2: Iterative
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        result = []

        # If there is right, add to the stack. Else do nothing.
        # If there is left, do something then continue going to left.
        # Else pop right and repeat.
        while root or stack:
            if root:
                result.append(root.val)
                if root.right:
                    stack.append(root.right)
                root = root.left
            else:
                root = stack.pop()      

        return result