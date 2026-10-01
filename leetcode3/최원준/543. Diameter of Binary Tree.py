# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#

'''
1. 아이디어 :
- 현재 노드를 포함한게 가장 길수도 있기에 왼쪽/오른쪽 중 깊은것 리턴
- 현재 노드 자식들을 계산한게 가장 길수도 있기에 왼쪽 깊이 + 오른쪽 깊이를 리턴


2. 시간복잡도 :
    O(n)

3. 자료구조/알고리즘 :
dfs

'''

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def max_length(node): #deepest, longest
            if not node:
                return 0, 0
            
            left_deepest, left_longest = max_length(node.left)
            right_deepest, right_longest = max_length(node.right)

            return max(left_deepest, right_deepest) + 1, max(left_longest, right_longest, left_deepest + right_deepest)

        return max_length(root)[1]
