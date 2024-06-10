# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def findGoodNodes(root, val):
            if not root:
                return 0
            
            if root.val >= val:
                val = max(val, root.val)
                return 1 + findGoodNodes(root.left, val) + findGoodNodes(root.right, val)
            else:
                return findGoodNodes(root.left, val) + findGoodNodes(root.right, val)

        return findGoodNodes(root, root.val)

# Alternative
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxVal):
            if not node:
                return 0

            res = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
            return res

        return dfs(root, root.val)
