# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Approach 1: DFS
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # Check if node is a leaf
        if not root.left and not root.right:
            return 1
        
        # If one of the children is null, assign the depth of the children to infinity instead of 0 
        # so that min() will work. 
        left = self.minDepth(root.left) if root.left else float('inf')
        right = self.minDepth(root.right) if root.right else float('inf')
        
        return min(left, right) + 1

# Approach 2: DFS, faster
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        if root.left and not root.right:
            return 1 + self.minDepth(root.left)
        if root.right and not root.left:
            return 1 + self.minDepth(root.right)

        return 1 + min(self.minDepth(root.left), self.minDepth(root.right)) 
    
# Approach 3: BFS
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: 
            return 0

        queue = [root]
        level = 0
        while queue:
            level +=1
            next_queue = []
            for node in queue:
                # Go through layer by layer and stop when a leaf is reached
                if not node.left and not node.right:
                    return level
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            queue = next_queue