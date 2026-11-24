# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: TreeNode | None, limit: int) -> TreeNode | None:
        
        def dfs(node, prev_total):
            if not node:
                return None
            
            node_total = prev_total + node.val
            
            if not node.left and not node.right: # leaf
                return node if node_total >= limit else None

            node.left = dfs(node.left, node_total)
            node.right = dfs(node.right, node_total)

            if not node.left and not node.right: # become leaf
                return None
            
            return node
        
        return dfs(root, 0)

