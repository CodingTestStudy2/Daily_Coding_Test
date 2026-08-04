# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.total = 0

        def reversed(node):
            if not node:
                return 
            
            reversed(node.right)

            self.total += node.val
            node.val = self.total

            reversed(node.left)
        
        reversed(root)
        return root