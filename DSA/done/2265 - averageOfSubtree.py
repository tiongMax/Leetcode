# https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        res = 0

        def dfs(n):
            nonlocal res
            if not n:
                return (0, 0)

            left, right = dfs(n.left), dfs(n.right)
            sum = left[0] + right[0] + n.val 
            cnt = left[1] + right[1] + 1

            if (sum // cnt) == n.val:
                res += 1
            
            return (sum, cnt)

        dfs(root)
        return res