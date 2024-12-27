# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Approach 1: Recursive
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        self.traverse(root, stack)
        return stack

    def traverse(self, node, stack):
        if not node:
            return stack
        
        self.traverse(node.left, stack)
        self.traverse(node.right, stack)
        stack.append(node.val)
        return stack
    
# Approach 2: Iterative
# Null will treated as a node and add into the stack.
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root] # Can use 1 stack only with element as tuple
        visit = [False]
        result = []

        while stack:
            curr, status = stack.pop(), visit.pop()
            if curr:
                if status: # If it is visited before
                    result.append(curr.val)
                else:
                    # Add into stack in this order as we want the left to pop first, then right, lastly
                    # mid to follow the postorder sequence.
                    # If left is added, it will be popped out immediately. Then we set its status to true 
                    # and add it back with its children in this sequence again. 
                    stack.append(curr)
                    visit.append(True)
                    stack.append(curr.right)
                    visit.append(False)
                    stack.append(curr.left)
                    visit.append(False)

        return result