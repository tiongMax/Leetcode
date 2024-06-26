# https://leetcode.com/problems/balance-a-binary-search-tree
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        inorder = []
        stack = []
        curr = root

        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                inorder.append(curr)
                curr = curr.right

        def dfs(s, e):
            if s > e:
                return None

            mid = s + (e - s) // 2
            root = TreeNode(inorder[mid].val)
            root.left = dfs(s, mid - 1)
            root.right = dfs(mid + 1, e)
            return root

        return dfs(0, len(inorder) - 1)

