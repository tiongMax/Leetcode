# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Approach 1: time: o(n), space: o(n)
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        def dfs(node, arr):
            if not node:
                return
            dfs(node.left, arr)
            arr.append(node)
            dfs(node.right, arr)

        arr = []
        # Run inorder dfs and store in an array. It should be sorted.
        dfs(root, arr)
        swap = []

        # Check for misplace and store it with its previous as a pair in an array.
        for i in range(1, len(arr)):
            if arr[i - 1].val > arr[i].val:
                swap.append([arr[i - 1], arr[i]])

        # Since the arr stores the reference of the note so we can swap them like this.
        # If there is only pair, swap the element in the pair.
        if len(swap) == 1:
            swap[0][0].val, swap[0][1].val = swap[0][1].val, swap[0][0].val
        # Else swap with the pair.
        else:
            swap[0][0].val, swap[1][1].val = swap[1][1].val, swap[0][0].val

# Approach 2:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, nodes):
        if not root:
            return 

        self.dfs(root.left, nodes)
        if nodes[3] and root.val < nodes[3].val:
            #  for the adjacent swap
            if not nodes[0]:
                nodes[0] = nodes[3]
                nodes[1] = root
            #  For the non adjacent swap
            else:
                nodes[2] = root
        nodes[3] = root
        self.dfs(root.right, nodes)

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        nodes = [None, None, None, TreeNode(float('-inf'))] # First, next of first, last, prev

        self.dfs(root, nodes) 
        if nodes[0] and nodes[2]:
            nodes[0].val, nodes[2].val = nodes[2].val, nodes[0].val
        elif nodes[0] and nodes[1]:
            nodes[0].val, nodes[1].val = nodes[1].val, nodes[0].val
