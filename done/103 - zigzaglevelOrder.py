# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        if not root:
            return res

        queue = [root]
        lvl = 0
        while queue:
            cur_lvl = []
            cur_res = []
            for i in range(len(queue)):
                cur_node = queue[i]
                cur_res.append(cur_node.val)

                if cur_node.left:
                    cur_lvl.append(cur_node.left)
                if cur_node.right:
                    cur_lvl.append(cur_node.right)

            if lvl % 2 != 0:
                cur_res = reversed(cur_res)
            queue = cur_lvl
            lvl += 1
            res.append(cur_res)

        return res