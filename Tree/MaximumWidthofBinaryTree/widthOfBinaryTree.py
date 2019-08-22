# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if root == None:
            return 0

        queue = [(root, 0, 0)]
        pos = cur_depth = left = 0
        res = 0

        for node, depth, pos in queue:
            if node != None:
                queue.append((node.left, depth+1, pos*2))
                queue.append((node.right, depth+1, pos*2+1))

                if depth != cur_depth:
                    cur_depth = depth
                    left = pos

                res = max(res, pos-left+1)

        return res