# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        if root is None:
            return None

        def dfs(c: TreeNode) -> TreeNode:
            print(c)
            val = c.val
            left = c.left
            right = c.right
            new_right = None
            new_left = None

            if left:
                new_right = dfs(left)
            if right:
                new_left = dfs(right)

            return TreeNode(val, new_left, new_right)

        return dfs(root)
