from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def equal(self,a:TreeNode, b:TreeNode):
        queue = deque()
        queue.append((a,b))
        while queue:
            x,y = queue.pop()

            if x is None and y:
                return False
            elif y is None and x:
                return False
            elif x.left is None and y.left:
                return False
            elif x.right is None and y.right:
                return False
            elif y.left is None and x.left:
                return False
            elif y.right is None and x.right:
                return False

            if x.val != y.val:
                return False

            if x.left and y.left:
                queue.append((x.left,y.left))
            if x.right and y.right:
                queue.append((x.right,y.right))

        return True                
                

    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        if self.equal(root,subRoot):
            return True

        queue = deque()
        queue.append(root)
        # print(subRoot)
        while queue:
            node = queue.popleft()
            left = node.left
            right = node.right
            # print(left,right)

            if self.equal(left,subRoot):
                return True
            if self.equal(right,subRoot):
                return True

            if left:
                queue.append(left)
            if right:
                queue.append(right)
        
        return False