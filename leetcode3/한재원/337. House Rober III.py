# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
- binary tree
- if the thief visits the current level, skip the next level
- if the thief skip the current level, thief can visit the next level or skip

   3
  / \ 
 4   5
 / \  \
1   3  1

3 + 1 + 3 + 1 = 8
4 + 5 = 9 => return 9

DFS
- visit / skip
- visit
    - can't visit the children
- skip
    - left child can visit/skip
    - right child can visit/skip

- return max (visit, current)

TC: O(N) / SC: O(N)
'''
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0
            
            visit_curr = node.val

            if node.left:  # if visit current, skip the next level
                visit_curr += dfs(node.left.left)
                visit_curr += dfs(node.left.right)
            
            if node.right:
                visit_curr += dfs(node.right.left)
                visit_curr += dfs(node.right.right)
            
            skip_curr = dfs(node.left) + dfs(node.right)

            return max(visit_curr, skip_curr)
                
    
        return dfs(root)
        